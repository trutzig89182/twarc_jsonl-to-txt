import json
import os
import jsonlines

tweetsnumber = 0
tweets = []

# scans all jsonl-files (with a specific language) and writes the tweet text and tweet-ID in a txt file
directory = os.getcwd()
for entry in os.scandir(directory):
    if entry.path.endswith(".jsonl") and entry.is_file():
        #print("file opened") #gibt "file opened" aus, wenn Datei geöffnet wurde (Kontrolle)
        with jsonlines.open(entry) as reader:
            for obj in reader:
                if not "retweeted_status" in obj:
                    # ##1 selects tweets by language
                    #if obj["lang"] == "de": ##1
                    if "full_text" in obj:  ##2
                        tweetsnumber = tweetsnumber + 1
                        print(tweetsnumber)
                        with open("tweets.txt", "a") as file:
                            gtid = obj["id_str"]
                            gttext = obj["full_text"]
                            gtentry = "(" + gtid + ") " + gttext + "\n"
                            file.write(gtentry)
