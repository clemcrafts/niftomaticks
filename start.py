import tweepy


class Nitftomatics:
    """
    Class in charge of analysing a NFT project
    """

    def __init__(self):
        """
        Setting up all the data needed for reporting.
        """
        self.tweeter = "KoalaAgencyNFT"

    def _get_tweeter_subscribers(self):
        """
        Getting the number of followers of the account.
        :return int followers: the number of followers of the account.
        """
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.get_user(self.tweeter)
        return user.followers_count

def start():
    """
    Start the application
    """
    niftomatics = Nitftomatics()
    tweeter_followers = niftomatics._get_tweeter_subscribers()
    print(f"The project has f{tweeter_followers} subscribers")

if __name__ == '__main__':
    start()
