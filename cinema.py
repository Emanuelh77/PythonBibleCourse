films = {
    'The Incredibles 2': [3,5],
    'The Equalizer 2': [18,5],
    'John Wick' : [18,5],
    'Infinity War': [12,5],
    'The big short': [12, 5]
    }

while True:
    movie = input("Hi!, what movie would you like to watch today? ").title()

    if movie in films:
        age = int(input("How old are you? ").strip())

        if age >= films[movie][0]:

            if films[movie][1] > 0:
                films[movie][1] -= 1
                print("Enjoy the film!")
            else:
                print("Sorry, we sold out!")
        else:
            print("You are not old enough for the film, sorry!")
    else:
        print("Oops, we currently don't have that film available, try another title!")
