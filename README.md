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
        - This version use a simple random() to generate the score and send to the game. This script needs to be executed before the daily tournament ends (every day at 18:00), and your wallet becomes the tournament' leader and receives the ARI (Manarium Token) prize