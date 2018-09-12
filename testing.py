users = ["Mark", "Peter", "Jason", "Jenn", "Kacie", "Alma", "Bruce", "Mark"]

name = input().strip().capitalize()

for i in range(0, len(users)):
        if users[i] == name:
            print("it worked")
