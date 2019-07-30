#Import PRAW: The Python Reddit API Wrapper. Be sure to first 'pip install praw'
import praw

#Create and authenticate your bot account. You can find the details on how to do this here: https://praw.readthedocs.io/en/latest/getting_started/authentication.html
#You can create your application on reddit here: https://www.reddit.com/prefs/apps/
#Following details are just the default, you have to change them for your account.
reddit = praw.Reddit(client_id='SI8pN3DSbt0zor',
                     client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                     password='1guiwevlfo00esyy',
                     user_agent='testscript by /u/fakebot3',
                     username='fakebot3')

scannedAuthors = [] #List of comment authors who have already been scanned and replied to. This is to avoid spamming the same person if they make more comments. It clears when the program is closed, but if you want to make it permanent you can save to a txt file and read from that.
querySubreddit = "anime" #Subreddit we are scanning for. If users post in this subreddit more than the threshold, then the bot replies to them.
postThreshold = 15

#Remove 'skip_existing=True' so that the bot runs on old messages as well, otherwise keep it True so that it only applies to new subreddits.
#You can add more subreddits that you wish for the bot to operate on by just adding it in as a parameter for subreddit e.g. 'gaming+pics+askreddit'
for comment in reddit.subreddit('gaming+movies').stream.comments(skip_existing=True):
    latestAuthor = str(comment.author) #The username of the author of the latest comment
    
    if latestAuthor not in scannedAuthors: #If this author has not already been "scanned" then the scan is done.
        noOfRelaventPosts = 0
        for usercomment in reddit.redditor(latestAuthor).comments.new(limit=150): #Go through the latest comment author's last 150 comments and check the subreddit it was posted in.
            if usercomment.subreddit == querySubreddit: #If the comment is posted in the subreddit you are scanning for, iterate noOfRelaventPosts by one.
                noOfRelaventPosts += 1

        if noOfRelaventPosts >= postThreshold: #If that author has 15 (the default threshold) or more comments in the subreddit we are scanning for, then reply to them with the custom message.
            comment.reply(latestAuthor+" has posted in "+querySubreddit+" "+str(noOfRelaventPosts)+" times.")

        else: #Otherwise, do nothing.
            pass

    print(latestAuthor+" has posted in "+querySubreddit+" "+str(noOfRelaventPosts)+" times.") #Prints to console for testing purposes.
        
    scannedAuthors.append(latestAuthor)
