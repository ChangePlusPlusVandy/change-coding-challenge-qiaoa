import base64
import requests
import random


def get_tweets():
    client_key = 'seYm4CirXupxLh6Wbx8nmxtrK'
    client_secret = 'SnvsZf5O7NYjZDE2h9AMQQmZcelHMdRd1iPsOM6QCGk5QW3O54'

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    # add functionality to check status code
    auth_resp.status_code

    # Keys in data response are token_type (bearer) and access_token (your access token)
    auth_resp.json().keys()

    access_token = auth_resp.json()['access_token']

    my_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    my_params = {
        'result_type': 'recent',
        'count': 3200,
        'exclude_replies': True,
        'include_rts': False
    }

    elon_resp = requests.get(
        "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk", params=my_params,
                               headers=my_headers)

    # add functionality to check status code
    elon_resp.status_code
    elon_data = elon_resp.json()

    kanye_resp = requests.get(
        "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=kanyewest", params=my_params,
                               headers=my_headers)

    # add functionality to check status code
    kanye_resp.status_code
    kanye_data = kanye_resp.json()

    all_tweets = []
    tweet_user = []

    for x in elon_data:
        all_tweets.append(x['text'])
        tweet_user.append('Elon Musk')

    for x in kanye_data:
        all_tweets.append(x['text'])
        tweet_user.append('Kanye West')

    return all_tweets, tweet_user


def main():
    all_tweets, tweet_user = get_tweets()
    continue_game = True
    attempts = 0
    correct = 0

    while continue_game:
        attempts += 1

        print("Guess who wrote this tweet!")

        # choose random tweet
        num = random.randint(0, len(all_tweets) - 1)
        ans = tweet_user[num]
        print(all_tweets[num])

        guess = input('Enter E for Elon Musk and K for Kanye West: ')
        guess = guess.strip()

        # validate guess
        while guess.lower() != 'e' and guess.lower() != 'k':
            print('Invalid input! Guess again')
            guess = input('Enter E for Elon Musk and K for Kanye West: ')
            guess = guess.strip()
        if guess.lower() == 'e':
            guess = 'Elon Musk'
        else:
            guess = 'Kanye West'

        print('You guessed ' + guess)

        if guess == ans:
            print('That was correct!')
            correct += 1
        else:
            print('Oops, wrong choice!')

        user_quit = input('Do you want to quit? Press Y or N: ')
        user_quit = user_quit.strip()
        # validate input
        while user_quit.lower() != 'y' and user_quit.lower() != 'n':
            user_quit = input('Invalid input! Press Y or N:')
            user_quit = user_quit.strip()
        if user_quit.lower() == 'y':
            print('Thanks for playing! Here are your results:')
            print('Correct guesses: ' + str(correct))
            print('Total attempts: ' + str(attempts))
            continue_game = False


if __name__ == "__main__":
    main()





