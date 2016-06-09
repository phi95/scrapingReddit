# Scraping Reddit

The purpose of this program is to scrape a subreddit for something specific.
The program will send an email (or text) when there is a new post containing
the word/phrase entered into the program.

## Prerequisite

The program uses PRAW (The Python Reddit API Wrapper), so that package must
be installed for this program to run.

Click [here](https://github.com/praw-dev/praw) for more details to install.

## How to run

The program is intended to be run as a bot. What this program does is that
it checks the newest post for what is searched for and writes the title of the
found post onto a text file. The next time the program checks it double checks
with the text file and if the title is different, the program will sent out an
email notification.

Use some form of task scheduler to automate the program.

Also be mindful of Reddit's terms such as no more than 1 request every 2 seconds.
