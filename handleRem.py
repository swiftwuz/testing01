tweet_ = 'welcome to github @swiftwuz'


def extractUser(tweet):
    handles = []
    handle = tweet.split(' ')
    for token in handle:
        if token[0] == '@':
            handles.append(token)
    return handles


print(extractUser(tweet_))
