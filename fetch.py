import tweepy,csv, datetime


class Fetch:
    """
    Class in charge of fetching data for a list of NFT projects.
    """

    def __init__(self):
        """
        Setting up all the data needed for reporting.
        """
        self.tweeters = ["larvalabs",
                         "artblocks_io",
                         "BoredApeYC",
                         "0n1Force",
                         "MyCurioCards",
                         "ParallelNFT",
                         "Pudgy_Penguins",
                         "coolcatsnft",
                         "KoalaAgencyNFT",
                         "punkscomic",
                         "satoshibles",
                         "GoonsNft",
                         "Aworld_NFT"]


    @staticmethod
    def _get_tweeter_subscribers(username):
        """
        Getting the number of followers of the account.
        :param str username: the tweeter username of the project.
        :return int followers: the number of followers of the account.
        """
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.get_user(username)
        return user.followers_count

    def write_csv(self):
        """
        Write CSV with the tweeter count of each project for a given date.
        """
        time = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%p")
        filename = 'reports/' + time + '.csv'
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["project", "tweeter_followers"])
            for project in self.tweeters:
                writer.writerow(
                    [project, self._get_tweeter_subscribers(project)])

def start():
    """
    Start the application
    """
    fetch = Fetch()
    fetch.write_csv()

if __name__ == '__main__':
    start()
