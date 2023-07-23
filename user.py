from datetime import datetime, timedelta

from post import Post
from comment import Comment
from reply import reply


class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.followed_users = set()
        self.posts = []
        self.comments = {}
        self.comments_id = 0

    def post_feed_item(self, post_id, content):
        timestamp = datetime.now()
        post = Post(post_id + 1, self.user_id, content, timestamp)
        self.posts.append(post)

    def follow(self, user):
        self.followed_users.add(user.user_id)

    def reply(self, post_id, content):
        timestamp = datetime.now()
        comment_id = self.comments_id + 1
        reply(comment_id, self.user_id, post_id, content, timestamp)
        # comment = Comment(comment_id, self.user_id, post_id, content, timestamp)
        # self.comments[post_id] = comment

    def upvote(self, post_or_comment):
        post_or_comment.upvotes += 1

    def downvote(self, post_or_comment):
        post_or_comment.downvotes += 1
