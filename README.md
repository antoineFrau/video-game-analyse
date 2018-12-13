# TP Big Data
This work able me to predict the game of the 2018 on PS4. Using Big Data methodologies.. Have Fun.
https://github.com/antoineFrau/video-game-analyse 

## Requirements
Use `pip 3 install` 

python==3.7
pip==3

tweepy==3.7.0

pytrends==4.4.0

textblob==0.15.2

matplotlib==3.0.2

numpy==1.15.4

pandas==0.23.4

You will need Twitter API account to use this project.

Change the line 9 to 12 in [main.py](main.py).
```
consumer_key = "YOUR_KEY_HERE"
consumer_secret = "YOUR_KEY_HERE"
access_token = "YOUR_KEY_HERE"
access_token_secret = "YOUR_KEY_HERE"
```

## Additionnal informations
Everything here has already been generated, if you want to regeneraet the data, you can run [main.py](main.py), will get absolutly needed informations in the [result.json](result.json) like the keyword for search prupose of the game and the release date.
Then it will generate all data in a specific folder for each game.

Finaly if you want to generate graphs you can run [graphics.py](graphics.py).

### Add a game
If you want to add a game or update one juste go to [result.json](result.json) and modyfy where it's write `HERE` : 
```
"game_name_HERE": {
    "release_date": "YYYY-MM-DD HERE",
    "nb_tweets": 0,
    "keyword": "Game Name HERE",
    "sentiment": [],
    "trends": {
        "start_at": "YYYY-MM-DD HERE",
        "end_at": "YYYY-MM-DD HERE",
        "cities": {},
        "evolutions": {}
    }
}
```
And don't forget about the line 10 of [graphics.py](graphics.py), add or modify the list of keys.
```
keys = ["game_name_HERE"]
```

## Author
Antoine Frau - Master 1 Développement Full-Stack.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details