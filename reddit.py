import praw
import numpy as np
import pandas as pd

# from traceback import format_exc, print_exc
import os
import argparse

from nlp import sentimentAnalyzer


# Import reddit info
reddit = praw.Reddit(
    client_id="Rl-KzGv-CAItNw",
    client_secret="QXsO7iF-RLCZi8RBSMf85mV_nUY",
    user_agent="testscript by /u/Ru8ted",
    username="Ru8ted",
    password="myguitarisold",
)

# MAKE ALL OF THIS A FUNCTION
# MAKE SURE ALL THE VARIABLES THATS DEFINED OUTSIDE SHOULD COME THROUGH
# ADD DOCSTRING TO FUNCTION
cwd = os.getcwd()


def get_reply(replies, level, index, data_comment):
    """
    This function gets the reply from a specified comment.
    Saves data to dataframe.

    Parameters:
    -----------------
    replies : praw.models.comment_forest.CommentForest
        A list-like object that stores the replies

    level : int
        A variable used to store the level of the reply

    index : int
        A temporary variable used to keep track of the index

    data_comment : pd.Dataframe
        A dataframe used to keep track of the comment's attributes

    Returns:
    -----------------
    index : int
        A temporary variable used to keep track of the index
    """
    # Reply is like a list type, loop through all replies
    for reply in replies:
        if type(reply) != praw.models.reddit.more.MoreComments:
            # add comment data from reddit API
            data_comment.loc[index, "author"] = reply.author
            data_comment.loc[index, "body"] = reply.body
            data_comment.loc[index, "created_utc"] = reply.created_utc
            data_comment.loc[index, "edited"] = reply.edited
            data_comment.loc[index, "id"] = reply.id
            data_comment.loc[index, "is_submitter"] = reply.is_submitter
            data_comment.loc[index, "parent_id"] = reply.parent_id
            data_comment.loc[index, "score"] = reply.score
            data_comment.loc[index, "stickied"] = reply.stickied
            data_comment.loc[index, "level"] = level
            index += 1
            
            # Reruns recursively to go through comment tree
            index = get_reply(reply.replies, level + 1, index, data_comment)
    return index


def get_comment(comments, index, data_comment):
    """
    This function gets the comment from a specified submission.
    Saves data to dataframe. Similar to get_reply.

    Parameters:
    -----------------
    comments : praw.models.comment_forest.CommentForest
        A list-like object that stores the comments

    index : int
        A temporary variable used to keep track of the index

    data_comment : pd.Dataframe
        A dataframe used to keep track of the comment's attributes

    Returns:
    -----------------
    None
    """

    # Loop through all comments
    for comment in comments:
        # Makes sure it is the right comment type
        if type(comment) != praw.models.reddit.more.MoreComments:
            # add comment data from reddit API
            print("\t\t\tcommments: ", comment.body, "\n", comment.author)
            data_comment.loc[index, "author"] = comment.author
            data_comment.loc[index, "body"] = comment.body
            data_comment.loc[index, "created_utc"] = comment.created_utc
            data_comment.loc[index, "edited"] = comment.edited
            data_comment.loc[index, "id"] = comment.id
            data_comment.loc[index, "is_submitter"] = comment.is_submitter
            data_comment.loc[index, "parent_id"] = comment.parent_id
            data_comment.loc[index, "score"] = comment.score
            data_comment.loc[index, "stickied"] = comment.stickied
            data_comment.loc[index, "level"] = 1
            index += 1

            # Reruns recursively to go through comment tree
            index = get_reply(comment.replies, 2, index, data_comment)


def get_submission(subreddits, category, path, n, mode):
    """
    This function scrapes the submissions from a specified subreddit(s).
    Saves data to CSV file.

    Parameters:
    -----------------
    subreddits : list
        A list of string subreddit names

    path : str
        The path for the saved csv file

    n : int
        The number of submissions you scrape from each catagory
        Default = 3

    mode : int
        Whether you want submissions, or submissions and comments
        1 = submissions
        2 = submissions and comments

    Returns:
    -----------------
    None
    """
    for sub in subreddits:
        print("sub: ", sub)
        subreddit = reddit.subreddit(sub)
        # catagories = ["controversial", "hot", "new", "rising", "top"]
        # catagories_new = [
        #     subreddit.controversial,
        #     subreddit.hot,
        #     subreddit.new,
        #     subreddit.rising,
        #     subreddit.top,
        # ]
        catagories = [category]

        # Uses category from user submission
        catagories_new = [
            # subreddit.hot
            eval(f"subreddit.{category}")
        ]

        # All specified perameters from reddit API
        columns = [
            "category",
            "title",
            "author",
            "sentiment",
            "selftext",
            "subreddit",
            "clicked",
            "url",
            "comments",
            "created_utc",
            "distinguished",
            "edited",
            "id",
            "is_original_content",
            "is_self",
            "link_flair_template_id",
            "link_flair_text",
            "locked",
            "name",
            "num_comments",
            "over_18",
            "permalink",
            "poll_data",
            "score",
            "spoiler",
            "stickied",
            "upvote_ratio",
        ]
        # create dataframe with all info from reddit
        data = pd.DataFrame(np.zeros([len(catagories) * n, len(columns)]), columns=columns)

        columns.pop(0)

        counter = 0

        # Loop through all categories
        for name, i in zip(catagories, catagories_new):
            print("\t",name)

            # Loop through all submissions
            for submission in i(limit=n):

                print("\t\tsubmission: ",submission.title ,submission.name)
                data.loc[counter, "category"] = catagories[counter // n]
                # print(counter)

                for j in columns:
                    # Checks for error
                    try:
                        # Check if it is sentiment, and uses NLP to analyze text
                        if j == "sentiment":
                            # average sentiment between title and selftext
                            value = (sentimentAnalyzer(submission.selftext) + sentimentAnalyzer(submission.title))/2
                            data.loc[counter, j] = value
                        else:
                            data.loc[counter, j] = eval(f"submission.{j}")
                    
                    except Exception:
                        pass

                counter += 1

                if mode == 2: # Getting comments
                    # Creating new dataframe for these comments
                    data_comment = pd.DataFrame(
                        np.zeros([999999, 10]),
                        columns=[
                            "author",
            "body", 
            "created_utc",
            "edited",
            "id",
            "is_submitter",
            "parent_id",
            "score",
            "stickied",
            "level",
            ],
                    )
                    index = 0

                    # print("Testing out comments section:")
                    # print(subreddit)
                    # subreddit = reddit.subreddit(subreddit[0])
                    get_comment(submission.comments, index, data_comment)

                    # Make new file for comments
                    try:
                        os.mkdir(os.sep.join([path, sub + "-submission comments"]))
                    except FileExistsError:
                        pass
                    # Packages it into CSV format
                    data_comment = data_comment.loc[data_comment["body"] != 0]
                    data_comment.to_csv(
                        os.sep.join([path, sub + "-submission comments", submission.name + ".csv"])
                    )

        print(data)

        # All work is in the exec or this section
        data = data.loc[data["title"] != 0]

    data["permalink"] = "reddit.com" + data["permalink"]

    # Download the data as csv
    data.to_csv(os.sep.join([path, "static", "reddit.csv"]))

    return data
    


if __name__ in "__main__":
    # It checks if your module is being run directly or being imported

    # ARGPARSE
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="This is a reddit data collection script."
        "The subreddit(s) selction can be changed with the subreddits.txt.",
    )

    # Gets mode, submissions, or submissions and comments
    parser.add_argument(
        "-m",
        "--mode",
        help="    choose mode:\n    1. Get Submissions\n    2. Get Submissions and Comments",
        choices=[1, 2],
        default=1,
        metavar="\b",
        type=int,
        required=True,
    )

    # Gets amount of submissions
    parser.add_argument(
        "-n",
        "--number",
        help="    enter the amount of submissions you scrape from each catagory (default = 10000)",
        default=3,
        metavar="\b",
        type=int,
    )
    
    # Gets location to save CSV
    parser.add_argument(
        "-d",
        "--directory",
        help="    put in your directory",
        default=os.getcwd(),
        metavar="\b",
        type=str,
    )

    # Updates these parameters
    args = parser.parse_args()
    mode = args.mode
    directory = args.directory
    n = args.number
    print(mode)
    print(directory)
    text_path = os.sep.join([directory, "subreddits.txt"])

