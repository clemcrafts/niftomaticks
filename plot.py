import tweepy,csv
import matplotlib.pyplot as plt


class Plot:
    """
    Class in charge of plotting the data for NFT projects.
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
        self.files = ['reports/2021_08_29-12_00_AM.csv',
                      'reports/2021_08_30-12_00_AM.csv']
        self.followers = {}
        self.growth = {}

    def load_project_followers(self):
        """
        Load projects followers.
        """
        for file in self.files:
            with open(file, 'r') as file:
                for line, row in enumerate(csv.reader(file)):
                    if line == 0:
                        continue
                    try:
                        self.followers[row[0]].append(row[1])
                    except KeyError:
                        self.followers[row[0]] = [row[1]]
        return self.followers

    def get_growth_rate(self):
        """
        Get average growth rate.
        """

        for project, followers in self.followers.items():
            init_followers = followers[0]
            growth_rate = 0
            for follower in followers[1:]:
                growth_rate = (float(follower)/float(init_followers)-1)*100
            self.growth[project] = growth_rate

    def plot_growth_rate(self):
        """
        Plot growth rate.
        """
        x_pos = [i for i, _ in enumerate(self.tweeters)]
        values = [self.growth[tweeters] for _, tweeters in enumerate(self.tweeters)]
        plt.bar(x_pos, values, color='blue')
        plt.xlabel("NFT projects")
        plt.ylabel("Growth rate (%)")
        plt.title("Average Tweeter growth rate for the last 1 day(s)")
        plt.xticks(x_pos, self.tweeters)
        plt.show()


if __name__ == '__main__':
    plot = Plot()
    plot.load_project_followers()
    plot.get_growth_rate()
    plot.plot_growth_rate()
