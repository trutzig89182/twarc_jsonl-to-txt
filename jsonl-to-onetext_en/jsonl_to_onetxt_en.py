import json
import os
import jsonlines
import gzip

tweetsnumber = 0
tweetsinfilecounter = 0
filenumber = 1
tweets = []

# scans all jsonl-files (with a specific language) and writes the tweet text and tweet-ID in a txt file within the created folder
#directory = os.getcwd()
#os.mkdir("results_txt_en/")
#writetweetstotxt(directory)

def writetweetstotxt(directory, month):
    if os.path.exists(directory + "/results_txt_en"):
        print("Folder " + directory + "/results_txt_en/ already exists. I move to the next folder. Check if tweets are already put into txt." )
    else:
        os.mkdir(directory + "/results_txt_en")
        # define variables
        tweetsnumber = 0
        tweetsselector = 0
        tweetsinfilecounter = 0
        filenumber = 1
        tweets = []
        for entry in os.scandir(directory):
            if entry.path.endswith(".jsonl.gz") and entry.is_file():
                #print("file opened") #gibt "file opened" aus, wenn Datei geöffnet wurde (Kontrolle)
                with gzip.open(entry, "rb") as jsonlentry:
                    reader = jsonlines.Reader(jsonlentry)
                    for obj in reader:
                        if not "retweeted_status" in obj:
                            if obj["lang"] == "en": # selects tweets by language
                                if "full_text" in obj:  # checks if new tweet in json object
                                    print(tweetsnumber)
                                    tweetsnumber += 1
                                    if tweetsselector == 51: # each 5th tweet is selected and printed in txt file
                                        tweetsselector = 0
                                        if tweetsinfilecounter == 99999:
                                            filenumber += 1
                                            tweetsinfilecounter = 0
                                        with open(directory + f"/results_txt_en/{month}_tweets_{filenumber}.txt", "a") as file:
                                            gtid = obj["id_str"]
                                            gttext_a = obj["full_text"]
                                            gttext = gttext_a.replace("\n", " <br> ") #replace löscht zeilenumbrüche
                                            gtentry = "<" + gtid + "> " + gttext + "\n\n"
                                            file.write(gtentry)
                                            tweetsinfilecounter += 1
                                    else:
                                        tweetsselector += 1


        # hängt Anzahl an in die Datei geschreiben tweets am Ende auskommentiert an die Datei ran.
        with open(directory + f"/results_txt_en/{month}_tweets_metadata.txt", "a") as file:
            gtentry = "< Total number of tweets in this folder: " + str(tweetsnumber) + ">"
            file.write(gtentry)
