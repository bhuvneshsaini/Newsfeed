from social_network import SocialNetwork
from utils import *


def main():
    social_network = SocialNetwork()

    while True:
        command_input = input("Enter a command: ")
        command_args = parse_command(command_input)

        command = command_args[0].lower()

        if command == "signup":
            username = command_args[1]
            password = command_args[2]
            social_network.signup(username, password)

        elif command == "login":
            username = command_args[1]
            password = command_args[2]
            try:
                social_network.login(username, password)
            except Exception as e:
                print("username or password incorrect, please try again!")

        elif command == "post":
            content = " ".join(command_args[1:])
            social_network.post_feed_item(content)

        elif command == "follow":
            username_to_follow = command_args[1]
            social_network.follow_user(username_to_follow)

        elif command == "reply":
            post_id = int(command_args[1])
            content = " ".join(command_args[2:])
            social_network.reply_to_post(post_id, content)

        elif command == "upvote":
            post_id = int(command_args[1])
            social_network.upvote_post(post_id)

        elif command == "downvote":
            post_id = int(command_args[1])
            social_network.downvote_post(post_id)

        elif command == "shownewsfeed":
            sorting_option = command_args[1].lower() if len(command_args) > 1 else "timestamp"
            social_network.display_news_feed(sorting_option)

        elif command == "users":
            social_network.get_users()

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
