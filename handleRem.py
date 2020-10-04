tweet1 = 'hey @_iampapa_ , @wuzcarti said you’re the most handsome person in the world but @kobyq doesn’t agree. what do you think?'
tweet2 = 'welcome to github @swiftwuz'
tweet3 = "@breh wag1"


# test function
def extractUser(tweet):
    handles = []
    handle = tweet.split(' ')
    for token in handle:
        if token[0] == '@':
            handles.append(token)
    return handles


print(extractUser(tweet1))
print(extractUser(tweet2))
print(extractUser(tweet3))


def get_user():
    pass
