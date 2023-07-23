from datetime import datetime, timedelta

from comment import Comment


class Post:

    def __init__(self, post_id, user_id, content, timestamp):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.upvotes = 0
        self.downvotes = 0
        #self.comments = []

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1

    @staticmethod
    def add_comment(comment_id, user_id, post_id, content, timestamp):
        timestamp = datetime.now()
        comment = Comment(comment_id, user_id, post_id, content, timestamp)
        return comment

    def get_time_ago(self):
        time_difference = datetime.now() - self.timestamp
        if time_difference < timedelta(seconds=60):
            return f"{time_difference.seconds}s ago"
        elif time_difference < timedelta(minutes=60):
            return f"{time_difference.seconds // 60}m ago"
        elif time_difference < timedelta(hours=24):
            return f"{time_difference.seconds // 3600} hr ago"
        else:
            return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Custom format for older timestamps