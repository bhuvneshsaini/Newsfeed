from post import Post

comments = {}
comments_count = {}


def reply(comment_id, user_id, post_id, content, timestamp):
    comment = Post.add_comment(comment_id, user_id, post_id, content, timestamp)
    comm = []
    comm.append(comment)

    if len(comments) == 0:
        comments[post_id] = comm
    else:
        comm = comments.get(post_id)
        if comm:
            comm.append(comment)
            comments[post_id] = comm
        else:
            comments[post_id] = comm

    comments_count[post_id] = len(comments.get(post_id))
