#import json
import os
import jsonlines
import gzip

germantweetsnumber = 0


directory = os.getcwd()
# generates subdirectory to put the generates files in
os.mkdir("txt_einzeln/")
for entry in os.scandir(directory):
    # selects all files that end with .jsonl.gz
    if entry.path.endswith(".jsonl.gz") and entry.is_file():
        # unzips file so we can work with it
        with gzip.open(entry, "rb") as jsonlentry:
            # opens file with jsonlines
            reader = jsonlines.Reader(jsonlentry)
            for obj in reader:
                # exludes retweets
                if not "retweeted_status" in obj:
                    # excludes tweets are not marked as German (Change "de" if
                    # you want to get tweets in another language).
                    if obj["lang"] == "de":
                        if "full_text" in obj:
                            # creates counter for the tweets writen in the subdirectory
                            germantweetsnumber = germantweetsnumber + 1
                            # prints counter in terminal for control
                            print(germantweetsnumber)
                            # gets TweetID for the file name
                            thistweet_id = obj["id_str"]
                            # writes the tweet’s full text into a txt file with TweetID as name
                            with open(f"txt_einzeln/{thistweet_id}.txt", "a") as file:
                                gtid = obj["id_str"]
                                gttext = obj["full_text"]
                                gtentry = gttext
                                file.write(gtentry)
