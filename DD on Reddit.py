import praw

list_of_posts = []

reddit = praw.Reddit(
    user_agent="<console:DD:0.5",
    client_id="",
    client_secret=""
)

subreddit = reddit.subreddit("RobinHoodPennyStocks+pennystocks")

for post in subreddit.new(limit=50):
    if ' DD ' in post.comments or post.title:
        list_of_posts.append(post.title)
        list_of_posts.append(post.url)
        list_of_posts.append('*********************')

for row in list_of_posts:
    print(row)
