known_users = ["Alice","Bob", "Claire", "Dan", "Emma", "Fred","Alice", "Georgie", "Harry"]

users = (len(known_users))

while True:
    print("Hi, my name is Travis")
    name = input("What is your name? " ).strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower().strip()

        if remove == "y":
            known_users.remove(name)
    else:
        print("Hmm I believe I have not met you yet {}.".format(name))
        addMe = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if addMe == 'y':
            known_users.append(name)
            print(known_users)

            

