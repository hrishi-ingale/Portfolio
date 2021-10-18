import praw
topic_name = input("Enter subreddit you want to search: ")
a = input("Enter keyword you want to search: ")
b = input("Enter the string to reply to comments: ")

client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

sub = reddit.subreddit(topic_name)
topic_name = sub.hot(limit=10)
# sub.subscribe()

for submission in (topic_name):
    if not submission.stickied:
        print("*************")
        print('Title: {}, ups: {}, downs: {}'.format(
            submission.title, submission.ups, submission.downs))
        # sub.upvote()

        for comment in submission.comments:
            if hasattr(comment, "body"):
                comment_lower = comment.body.lower()
                if a in comment_lower:
                    print("------------")
                    print(comment.body)
                    comment.upvote(b)
                    comment.reply(b)