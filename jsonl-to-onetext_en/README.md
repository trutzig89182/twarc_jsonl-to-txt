[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# twarc_jsonl-to-txt

Simple Python-script that writes tweets from jsonl files into a simple txt file for easy text analysis.

The twarc tools for collecting twitter data produce jsonl files. For analysis the data with the Corpus analysis tool “AntConc” I needed simple txt files. The script provides the data as plain txt, so it is readable by AntConc (https://www.laurenceanthony.net/software/antconc/).

The "jsonl-to-onetxt_en.py" script scans the given folder for jsonl files and writes only the tweet-IDs and the tweets full text into a text file that is more easy to handle. Optionally the tweets can be filtered by a language code (“en” for English preselected here – for other language codes, see: https://developer.twitter.com/en/docs/twitter-api/v1/developer-utilities/supported-languages/api-reference/get-help-languages).

With automated_script this process can be automated for an array of subfolders of the given directory which contain gzipped jsonl files.


Result:

&lt;Tweet-ID1&gt; Full text of tweet 1

&lt;Tweet-ID2&gt; Full text of tweet 2
…

The angle brackets should be recognized by AntConc as tags and not included in the word counting.
The script writes tweets into a seperate txt-file in the subdirectory “results_txt_en/”.

# How to use the scripts

Make sure you have Python 3.8 and the packages for jsonlines and gzip installed.

Copy the script to the folder your jsonl or jsonl.gz files are in or, if you use the automated script into a parent folder.

Make shure there is no subdirectory named "./results_txt_en/" in the (sub-) folder(s) or rename the directory in the script.

Open the folder with a shell. Type "python jsonl-to-onetxt_en.py" or "python automated_script.py" and push enter. You should see the counter of the tweets writen in the subdirectory start in your terminal window.

Go to the subirectory "./results_txt_en/" to get the resulting txt file.




[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
