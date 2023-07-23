from user import User
from reply import *


class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.users_id = {}
        self.posts_id = {}
        self.current_user = None
        self.post_id = 0

    def signup(self, username, password):
        user_id = len(self.users) + 1
        new_user = User(user_id, username, password)
        self.users[username] = new_user
        self.users_id[user_id] = username
        print(f"User '{username}' signed up successfully.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            print(f"Welcome, {self.current_user.username}!")
        else:
            print("Invalid username or password.")

    def display_news_feed(self, sorting_option):
        if not self.current_user:
            print("Please login first to view the news feed.")
            return

        sorted_feed = self.sort_news_feed(sorting_option)
        for post in sorted_feed:

            username = self.users_id.get(post.user_id)

            user = self.users.get(username)
            print(f"User: {username}, User Id: {post.user_id}, Post Id: {post.post_id}, Post: {post.content}, "
                  f"Upvotes: {post.upvotes}, Downvotes: {post.downvotes}, "
                  f"Comments Number: {comments_count.get(post.post_id,0)}, Time: {post.get_time_ago()}")

            if comments.get(post.post_id,0) != 0:

                for comment in comments.get(post.post_id):
                    print(f"Comments : ")
                    print(f"User: {comment.user_id}, {comment.content}")

    def post_feed_item(self, content):
        if not self.current_user:
            print("Please login first to post.")
            return

        self.current_user.post_feed_item(self.post_id, content)
        self.post_id += 1
        self.posts_id[self.post_id] = self.current_user.user_id

        print("Posted successfully.")

    def follow_user(self, username_to_follow):
        if not self.current_user:
            print("Please login first to follow users.")
            return

        if username_to_follow in self.users:
            user_to_follow = self.users[username_to_follow]
            self.current_user.follow(user_to_follow)
            print(f"You are now following '{username_to_follow}'.")
        else:
            print(f"User '{username_to_follow}' not found.")

    def reply_to_post(self, post_id, content):
        if not self.current_user:
            print("Please login first to reply.")
            return

        user_id = self.posts_id.get(post_id)
        username = self.users_id.get(user_id)
        user = self.users.get(username)

        for post in user.posts:
            if post.post_id == post_id:
                self.current_user.reply(post_id, content)
                print("Replied successfully.")
                return

        print(f"Post with ID {post_id} not found.")

    def upvote_post(self, post_id):
        if not self.current_user:
            print("Please login first to upvote.")
            return

        user_id = self.posts_id.get(post_id)
        username = self.users_id.get(user_id)
        user = self.users.get(username)

        for post in user.posts:
            if post.post_id == post_id:
                self.current_user.upvote(post)
                print("Upvoted successfully.")
                return

        print(f"Post with ID {post_id} not found.")

    def downvote_post(self, post_id):
        if not self.current_user:
            print("Please login first to downvote.")
            return

        for post in self.current_user.posts:
            if post.post_id == post_id:
                self.current_user.downvote(post)
                print("Downvoted successfully.")
                return

        print(f"Post with ID {post_id} not found.")

    def sort_news_feed(self, sorting_option):
        if not self.current_user:
            return []

        if sorting_option == "followed_users":
            sorted_feed = sorted(self.current_user.posts + self.get_followed_users_posts(),
                                 key=lambda post: (post.user_id in self.current_user.followed_users, post.timestamp),
                                 reverse=True)
        elif sorting_option == "score":
            sorted_feed = sorted(self.current_user.posts + self.get_followed_users_posts(),
                                 key=lambda post: (post.upvotes - post.downvotes, post.timestamp),
                                 reverse=True)
        elif sorting_option == "comments":
            sorted_feed = sorted(self.current_user.posts + self.get_followed_users_posts(),
                                 key=lambda post: (len(post.comments), post.timestamp),
                                 reverse=True)
        else:
            sorted_feed = sorted(self.current_user.posts + self.get_followed_users_posts(),
                                 key=lambda post: post.timestamp, reverse=True)

        return sorted_feed

    def get_followed_users_posts(self):
        followed_posts = []
        for user in self.users.values():
            if user.user_id in self.current_user.followed_users:
                followed_posts.extend(user.posts)
        return followed_posts

    def get_users(self):
        if not self.current_user:
            print("Please login first to view usernames")
            return
        for user in self.users.values():
            print(user.username)
