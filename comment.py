
class Comment:
    def __init__(self, comment_id, user_id, post_id, content, timestamp):
        self.comment_id = comment_id
        self.user_id = user_id
        self.post_id = post_id
        self.content = content
        self.timestamp = timestamp
        self.upvotes = 0
        self.downvotes = 0

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes += 1