To add in the future:
- validate that the status code is 200 for all requests
- when scanning through the responses, remove those with media urls
- find a more space efficient way to hold the data for the tweets - the tweet_user list is very ineffective
- in main, ask user what 2 users they want, pass the usernames as strings to the get_tweets function. Replace Kanye and Elon with those strings