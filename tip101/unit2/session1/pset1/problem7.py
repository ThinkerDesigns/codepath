# WIP - need to find out how to reference a specific index of a specific key
def highest_rated(books):
    rating = 0
    result = {}
    for x in range(len(books)):
        if books["rating"][x] > rating:
            rating = books["rating"][x]
            result["title"] = books["title"][x]
            result["author"] = books["author"][x]
            result["rating"] = books["rating"][x]
        else:
            continue
    return result
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))