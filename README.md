# manarium-bot
This is a Bot to Hack the Games of Manarium (manarium.com/games)...

Was developed to proof the existence of a vulnerability in their system that allows an user to manipulate the scores and ever win the daily tournament, with a profit of 30x in a day, and works in all the 3 games in the platform.

Changelog:
    
    * v0:
        - Manarium used a Google Firebase instance to save the player' scores
        - Their hardcoded the credentials in the source-code, so it was used to generate a JWT and send the request to the Firebase instance.
        - Initially, the manipulation could be made via DevTools after simply send the following command: 
        - await firebase.firestore().collection("GAME_NAME").doc("WALLET_ADDRESS").set(JSON.parse("{\"wallet\":\"WALLET_ADDRESS\",\"score\":SCORE}"));

    * v1:
        - The first version of bot was created because the script in DevTools doesn't working anymore, but the same infra remains.
        - This version use a simple random() to generate the score and send to the game. This script needs to be executed before the daily tournament ends (every day at 18:00), and your wallet becomes the tournament' leader and receives the ARI (Manarium Token) prize.
    
    * v2:
        - At this time, I've already reported this vulnerability to Manarium' Team and their fixed. After 2 days of maintenance to fix the vulnerability, the game waked up again, with the new "Anti-Cheat" protection... Sounds good no? :P
        - After (I think), 1-2 hours, I found a bypass and could manipulate again the scores.
        - Their migrate the Firebase to a private instance and did the following "fix": 
            * Hardcoded (Again) a passphrase that will return the JWT... This JWT is used to authenticate in their back-end and sent the data.
            * The request to update the score now needs the JWT and the body of the request is a base64 code containing the following information:
                * gameTitle: The name of game
                * wallet: The player' wallet
                * sessionTime: The time that the user "spent" in the game (Maybe monitored by their anti-cheat)
                * timeUTC: The current time
                * ip: The user' ip
                * gameVersion: The version of the game
                * score: The user' score
            * The payload will be something like:
                * base64.encode(JSON.parse({"gameTitle":"Game Name", "wallet": "User Wallet", "sessionTime": "Time Spent", "timeUTC": "Current Time", "ip": "Some Ip Address", "gameVersion": "2", "score": SCORE}))
        - As the passphrase still hardcoded, I was able to manipulate again my score by using the following methodology (My Choice):
            * The sessionTime will be the score * 2.03 seconds
                * I've choiced this number to simulate a player that makes 1 point every 2 seconds
            * The IP was a random IP address
            * The score now it's calculated in this way:
                * last_score = 1 (The first score of the user in the tournament)
                * session_time = (last_score * 2.03) + random.randint(0,9) + random.random()
                    * I've used in this way just to be a bit random from each request :)
            * Send the Request with the generated data...
            * After sent, the script will sleep for session_time + 7.34 seconds.
                * This sleep simulate the end and re-entering in the game
                * 7 seconds is the time approximately that this action takes, added 0.34 to be more "aleatory".
            * After sleep, the script will check the scoreboard to see if the user is the tournamet leader, if not these steps will be did again, and the last_score will be:
                * last_score = last_score + random.randint(3, 12)
                * 3 - 12 to be a more "human" score
            * If the user is the tournament leader, the script will sleep for 1 hour + some random minutes
                * This simulates that the player after being the leader, stopped to play for this time.
                