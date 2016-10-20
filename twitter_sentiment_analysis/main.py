from twitter_sentiment_analysis.utilities import bcolors
from twitter_sentiment_analysis import tweets


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


def main_loop():
    print(get_header())
    print(get_info_warning())

    # Keep prompting for correct code
    incorrect_code = False
    while not incorrect_code:
        tweets.init_api()

main_loop()