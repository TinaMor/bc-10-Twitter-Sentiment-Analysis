from twitter_sentiment_analysis.utilities import bcolors
from twitter_sentiment_analysis import tweets
from twitter_sentiment_analysis import process_tweets
import subprocess
from tqdm import tqdm
import  time


def get_header():
    """
     Returns the header string.
     Will have this persist in across the application
     """
    title = """
 ___                         __
  |      o _|_ _|_  _  ._   (_   _  ._ _|_ o ._ _   _  ._ _|_    /\  ._   _. |     _ o  _
  | \/\/ |  |_  |_ (/_ |    __) (/_ | | |_ | | | | (/_ | | |_   /--\ | | (_| | \/ _> | _>
                                                                               /"""

    sub_title = "Get sentiments from your tweets fast and easy!"
    header = bcolors.HEADER + title + bcolors.ENDC + "\n" + bcolors.WARNING + "\t\t" + sub_title + bcolors.ENDC + "\n"
    return header


def get_info_warning():
    top = "\t*-------------------------------------------------------------*"
    warn = """\tThis application will to access your Twitter account.
\tTo do that, the application needs explicit permission from you.
\tA URL will be given, with which Twitter will give a a verification
\tcode to give this application access.
    """
    note = "\tTHIS APPLICATION WILL NOT POST ANY DATA TO YOUR TIMELINE."
    res = bcolors.BOLD + top + "\n"
    res += warn + bcolors.FAIL + "\n" + note + bcolors.ENDC + '\n' + bcolors.BOLD + top + "\n" + bcolors.ENDC
    return res


def get_personal_info():
    user = tweets.get_user_info()
    print(bcolors.UNDERLINE, "Personal Details:", bcolors.ENDC, "\n")
    nm = user['name']
    name = ' '.join([n.capitalize() for n in nm.split(' ')])
    print(bcolors.OKBLUE, "Name:", bcolors.ENDC, bcolors.OKGREEN, name, bcolors.ENDC, bcolors.OKBLUE,
          "\tTwitter Handle: ",
          bcolors.ENDC, bcolors.OKGREEN, "@", user['screen_name'], bcolors.OKBLUE, "Number of Tweets: ", bcolors.ENDC,
          bcolors.OKGREEN, user['statuses_count'], bcolors.ENDC,
          bcolors.OKBLUE, "Number of Followers: ", bcolors.ENDC, bcolors.OKGREEN, user['followers_count'], bcolors.ENDC)
    print(bcolors.OKBLUE, "Latest Tweet:", bcolors.ENDC, bcolors.BOLD, user['status']['text'], bcolors.ENDC + "\n")


def main_loop():
    while True:
        # do all
        print(get_header())
        print(get_info_warning())

        # Keep prompting for correct code
        tweets.init_api()

        # clear screen, print header
        subprocess.call('clear', shell=True)
        print(get_header())

        # print personal info
        get_personal_info()

        # Ask user for tweets to retrieve
        print(bcolors.BOLD, "+------------------------------------------------------------------------+", bcolors.ENDC)
        print(bcolors.BOLD, "\tThe application is ready.", bcolors.ENDC)
        print(bcolors.WARNING, "\tHow many tweets do you want to retrieve to analyse? Enter number below:",
              bcolors.ENDC)
        # TODO : Should check if tweets are already saved.
        # TODO : Do error checking here
        num_tweets = input(bcolors.OKGREEN + "\tEnter number of tweets (Default = 200): ")
        while True:
            if num_tweets == "":
                num_of_tweets = 200
                break
            else:
                try:
                    num_of_tweets = int(num_tweets)
                    break
                except ValueError:
                    print(bcolors.FAIL, "You entered an invalid number of tweets.")
                    num_tweets = input(bcolors.OKGREEN + "\tEnter number of tweets (Default = 200): ")

        # Load the tweets to tweets_list
        tweets.load_next_n_tweets(num_of_tweets)

        # save to json file
        tweets.save_tweets_json_file()

        # count frequency of words
        words_freq_counter = process_tweets.get_word_frequency(tweets.tweets_list)

        all_tweets_text = process_tweets.get_tweet_texts(tweets.tweets_list)

        # get emotions
        emotions = process_tweets.get_emotion_analysis(all_tweets_text)

        # get overall sentiment
        sentiment = process_tweets.get_overall_sentiment(all_tweets_text)

        # keep user waiting for 1 sec
        print(bcolors.OKBLUE, "Getting ready to perform sentiment analysis")
        for i in tqdm(range(100), desc="Processing:", unit=""):
            time.sleep(0.05)

        # Display Results
        # clear screen, display header
        subprocess.call('clear', shell=True)
        print(get_header())

        print(bcolors.HEADER, "\tSentiment Analysis -- Emotions", bcolors.ENDC)
        print(bcolors.BOLD, "\t\tType\t%Detected", bcolors.ENDC)
        for e in emotions['docEmotions'].items():
            data = bcolors.OKBLUE + "\t{: >10}\t" + bcolors.ENDC + bcolors.OKGREEN + "{:.2%}" + bcolors.ENDC
            print(data.format(e[0].capitalize(), float(e[1])))
        print(bcolors.BOLD, "+---------------------------------------------------------------+")
        print(bcolors.BOLD, "The overall sentiment expressed from your tweets is ", bcolors.ENDC, bcolors.WARNING,
              sentiment['docSentiment']['type'], bcolors.ENDC)
        print(bcolors.FAIL,
              "\nNOTE: This result is totally UNSCIENTIFIC and DOES NOT in any way represent who you are!",
              bcolors.ENDC)

        # Print the 10 most used words
        print(bcolors.BOLD, "+---------------------------------------------------------------+")
        print(bcolors.BOLD, "For better insight, these are the top 10 words you tweeted:", bcolors.ENDC)
        print(bcolors.HEADER, "Ten Most Tweeted Words", bcolors.ENDC)
        print(bcolors.BOLD, "\t\tWord\tFrequency", bcolors.ENDC)
        for t in words_freq_counter.most_common(10):
            data = bcolors.OKBLUE + '\t' + "{: >15}" + bcolors.ENDC + '\t' + bcolors.OKGREEN + "{:>5}" + bcolors.ENDC
            print(data.format(t[0], t[1]))
        print(bcolors.BOLD, "+---------------------------------------------------------------+", bcolors.ENDC)

        choice = input(bcolors.FAIL+ "\nWould you like to analyse a different account? (yes/no): "+ bcolors.WARNING)
        if choice in ('n', 'NO', 'No', 'no'):
            # clear screen
            subprocess.call('clear', shell=True)
            bye =  """

 _____                 _  ______
|  __ \               | | | ___
| |  \/ ___   ___   __| | | |_/ /_   _  ___
| | __ / _ \ / _ \ / _` | | ___ \ | | |/ _
| |_\ \ (_) | (_) | (_| | | |_/ / |_| |  __/
 \____/\___/ \___/ \__,_| \____/ \__, |\___|
                                  __/ |
                                 |___/       """
            print(bcolors.BOLD, bye, bcolors.ENDC)
            print(bcolors.OKGREEN, "\nFind me on Twitter at @kamau_michael", bcolors.ENDC)
            break
        elif choice in ('Yes', 'yes', 'y', 'YES'):
            subprocess.call('clear', shell=True)
        else:
            subprocess.call('clear', shell=True)
            break






