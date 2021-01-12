# twarc_jsonl-to-txt

Simple Python-script that writes tweets from jsonl files into a simple txt file for easy text analysis.
The twarc tools for collecting twitter data produce jsonl files. However, for analysis the data with the Corpus analysis tool AntConc I needed simple txt files. The script scans the given folder for jsonl files and writes only the tweet-IDs and the tweets full text into a text file that is more easy to handle. Optionally the tweets can be filtered by a language code.

Result:

(Tweet-ID1) Full text of tweet 1

(Tweet-ID2) Full text of tweet 2
…
