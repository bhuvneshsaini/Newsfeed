# Demo Of Newsfeed App

This is a simple console-based social network application that allows users to interact with a social network. Users can signup, login, post content, follow other users, and view their news feed.

## Instructions

1. **Signup**: To create a new account, enter the following command: signup \<username> \<password>

2. **Login**: To login to an existing account, use the following command: login \<username> \<password>


3. **Post**: After logging in, you can post your content using the command:
post \<content>

4. **View users**: You can view the users using the command: users

5**Follow**: To follow another user, enter:
   follow \<followee_username>



5. **Show News Feed**: To view your news feed, you can sort the feed based on different criteria:
- To view posts from followed users first:
  ```
  shownewsfeed followed_users
  ```

- To sort by post scores (upvotes - downvotes):
  ```
  shownewsfeed scores
  ```

- To sort by the number of comments on each post:
  ```
  shownewsfeed comments
  ```

- To view the default news feed (sorted by timestamp, most recent first):
  ```
  shownewsfeed
  ```

6. **Reply or Comment**: To reply to a post or comment on a post, use the following command:
reply \<post_id> \<content>

   You can reply to a post using its ID, and your reply will be displayed along with the post.

## Getting Started

1. Clone the repository to your local machine.

2. Open the terminal/command prompt in the project directory.

3. Run the `main.py` file to start the social network console app.

4. Follow the above instructions to use the different features of the social network.

## Dependencies

This project is implemented in Python3. Make sure you have Python3 installed on your machine to run the application.

