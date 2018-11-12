
def slicer():
    #get user email address

    email = input("What is your email address?: ").strip()

    #slice out user name

    username = email[:email.index("@")]

    #slice domain name

    domainName = email[email.index("@") + 1:]

    #format message

    output = "Your username is {} and your domain is {}".format(username, domainName)

    #display output message

    print(output)

slicer()