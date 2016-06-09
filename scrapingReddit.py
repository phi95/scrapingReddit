"""
scrapingReddit
Author: Phi Long Nguyen
The purpose of this program is to scrape a subreddit for something specific.
The program will send an email (or text) when there is a new post containing
the word/phrase entered into the program.
"""
import praw
import smtplib

#Just a name for the bot, can be anything. Here because it is required.
user_agent = 'Scraper 0.1'

#Enter the login and server information for the mail service to outgo
usrname = 'email@email.com'
password = 'password'
server = 'smtp.gmail.com:587'

#The to and from email addresses
fromAddr = 'email@email.com'
toAddr = 'email@email.com'

#The subreddit name to search and the item/phrase to search for
subreddit_name = 'buildapcsales'
toLook = 'SSD'

################################################################################

r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit(subreddit_name)
check = None

#try reading the latest thing that was read
try:
    f = open('check', encoding = 'utf-8')
    check = f.read()
    f.close()
except:
    pass

for submission in subreddit.get_new(limit = 1):
    if check is not None and submission.title in check:
        break
    if toLook.lower() in submission.title.lower():
        print('found')
        f = open('check', 'w')
        f.write(submission.title)
        f.close()
        msg = ('\nWhat you were looking for is found: ' + submission.url)
        mailServer = smtplib.SMTP(server)
        mailServer.starttls()
        mailServer.login(usrname, password)
        mailServer.sendmail(fromAddr, toAddr, msg)
        mailServer.quit()
