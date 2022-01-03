import praw
import pathlib

secrets_path = pathlib.Path.cwd() / '.env'
with open(secrets_path,'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        attribute, value = tuple(line.split('='))  
        if 'USER' in attribute:
            REDDIT_USER = value.strip()
        elif 'PASSWORD' in attribute: 
            REDDIT_PASSWORD = value.strip()
        elif 'SECRET' in attribute:
            REDDIT_SECRET = value.strip()
        elif 'CLIENT_ID' in attribute:
            CLIENT_ID= value.strip()

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent="<console:SARCASM:0.1",
    username=REDDIT_USER,
    password=REDDIT_PASSWORD,
)

for submission in reddit.subreddit("learnpython").hot(limit=2):
    print('-----------------')
    print(submission.title)
    print(submission)
    for top_comment in submission.comments:
        print(top_comment)
        comment_tree = praw.models.comment_forest.CommentForest(top_comment)
        print(list(comment_tree))
        
        # break
        # for comment in comment_tree:
            
            # if not submission.id in comment.parent_id:
            #     print('**')
            #     print(comment.body)
            #     print(comment.parent_id)
            #         # print(reddit.comment(comment.parent_id.split('_')[1]).body)
            #     break
            
