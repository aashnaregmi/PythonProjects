import random
celebrity_list = [
    {
        "name": "Taylor Swift",
        "location": "New York, USA",
        "work": "Singer, Songwriter",
        "followers": 274_000_000
    },
    {
        "name": "Selena Gomez",
        "location": "Los Angeles, California, USA",
        "work": "Singer, Actress, Businesswoman",
        "followers": 418_000_000
    },
    {
        "name": "Kim Kardashian",
        "location": "Los Angeles, California, USA",
        "work": "Media Personality, Businesswoman",
        "followers": 355_000_000
    },
    {
        "name": "Zendaya",
        "location": "Los Angeles, California, USA",
        "work": "Actress, Singer",
        "followers": 177_000_000
    },
    {
        "name": "Jennifer Aniston",
        "location": "Los Angeles, California, USA",
        "work": "Actress, Producer",
        "followers": 44_300_000
    },
    {
        "name": "Hailey Bieber",
        "location": "Los Angeles, California, USA",
        "work": "Model, Businesswoman",
        "followers": 55_500_000
    }
]


for celebrity in celebrity_list:
    print(celebrity["name"])
    print(celebrity["location"])
    print(celebrity["followers"])
    print()


