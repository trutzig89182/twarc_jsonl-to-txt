[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# twarc_jsonl-to-txt

Simple Python-script that writes tweets from jsonl files into a simple txt file for easy text analysis.
The twarc tools for collecting twitter data produce jsonl files. However, for analysis the data with the Corpus analysis tool AntConc I needed simple txt files. 

The "jsonl-to-onetxt.py" script scans the given folder for jsonl files and writes only the tweet-IDs and the tweets full text into a text file that is more easy to handle. Optionally the tweets can be filtered by a language code.

Result:

(Tweet-ID1) Full text of tweet 1

(Tweet-ID2) Full text of tweet 2
…

The "json-gz-to-txt" script writes tweets from gzipped jsonl-files into a seperate txt-file for each tweet, where the file name is the Tweet-ID, while the file contains the Tweets full text. This allows for a better seperation of tweets when using AntConc.

# How to use the scripts

Make sure you have Python 3.8 and the packages for jsonlines and gzip installed.

Copy the script to the folder your jsonl or jsonl.gz files are in. 

Make shure there is no subdirectory named "./txt_einzeln/" or rename the directory in the script.

Open the folder with terminal. Type "python jsonl-gz-to-txt.py" or "python jsonl-to-onetxt.py" and push enter. You should see the counter of the tweets writen in the subdirectory start in your terminal window.

Go to the subirectory "./txt_einzeln" to get the txt files.




[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
