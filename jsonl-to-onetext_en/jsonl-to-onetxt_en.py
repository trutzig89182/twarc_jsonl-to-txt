import json
import os
import jsonlines
import gzip

tweetsnumber = 0
tweets = []

# scans all jsonl-files (with a specific language) and writes the tweet text and tweet-ID in a txt file within the created folder
directory = os.getcwd()
os.mkdir("results_txt_en/")

seperator = "stopñä stopñä stopñä stopñä stopñä stopñä stopñä stopñä stopñä"
for entry in os.scandir(directory):
    if entry.path.endswith(".jsonl.gz") and entry.is_file():
        #print("file opened") #gibt "file opened" aus, wenn Datei geöffnet wurde (Kontrolle)
        with gzip.open(entry, "rb") as jsonlentry:
            reader = jsonlines.Reader(jsonlentry)
            for obj in reader:
                if not "retweeted_status" in obj:
                    if obj["lang"] == "en": # selects tweets by language
                        if "full_text" in obj:  # checks if new tweet in json object
                            tweetsnumber = tweetsnumber + 1
                            print(tweetsnumber)
                            with open(f"results_txt_en/tweets.txt", "a") as file:
                                gtid = obj["id_str"]
                                gttext = obj["full_text"]
                                gtentry = "<" + gtid + "> " + gttext + "\n\n" + seperator + "\n\n"
                                file.write(gtentry)
# hängt Anzahl an in die Datei geschreiben tweets am Ende auskommentiert an die Datei ran.
with open(f"results_txt_en/tweets.txt", "a") as file:
    gtentry = "< Total number of tweets in this file: " + tweetsnumber + ">"
    file.write(gtentry)
