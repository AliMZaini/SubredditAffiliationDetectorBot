# SubredditAffiliationDetectorBot
Replies to users so others can see if they post on certain subreddits, similar to [/u/chapodetectorbot](https://www.reddit.com/user/chapodetectorbot)

# Requirements & Installation
1. Must have 'praw' installed, so just do 'pip install praw'
2. Must have python 3+ installed
3. Must have a reddit account and created an application there

# Explaination
This bot works similarly to 'chapodetectorbot' and there are many out there similar to it. This was made to practice basic praw and could be adapted to do all sorts of other things very easily.

If you do want to use it for it's current purpose, the current example on the code is with querySubreddit as 'anime' and the subreddits being scanned as 'gaming' and 'movies'. You can think of this as finding users who commonly post on /r/anime but are posting on /r/gaming or /r/movies. You can use it for something similar to 'chapodetectorbot' or adapt it to your own uses.

# Other
To read more about how to set up and use praw, go here: https://praw.readthedocs.io/en/latest/index.html

To create your application on reddit and get the client_id and client_secret, go here: https://www.reddit.com/prefs/apps/

If you make a new account and don't have enough karma to post in most subreddits, you can try this subreddit: https://www.reddit.com/r/FreeKarma4U/
