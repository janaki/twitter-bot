# twitter-bot
This a twitter bot, written in python, based on this [Blog Post](http://blog.mollywhite.net/twitter-bots-pt1/). 
This bot will scrape a google query for Darjeeling, Sikkum, and Assam, and send tweets to the [@selvisound](https://twitter.com/selvisound)  twitter account. 

I used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to scrape the google search results, then the python module [Tweepy](http://www.tweepy.org/) to access the Twitter Api. 

To run, you will need to have a twitter account, and a twitter app enabled with access tockens. Once that this is done you can run the bot: 

```python bots.py```
