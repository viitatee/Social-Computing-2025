def recommend(user_id, posts, reactions, follows):
    """
    Recommend 5 posts for a user.
    
    Parameters:
    - user_id: int, the current user
    - posts: list of dicts, each with 'id', 'user_id', 'content'
    - reactions: list of dicts, each with 'user_id', 'post_id', 'reaction_type'
    - follows: list of tuples (follower_id, followed_id)
    
    Returns:
    - list of 5 recommended post IDs
    """

    #Posts the user reacted positively to
    positive_posts = {r['post_id'] for r in reactions if r['user_id'] == user_id and r['reaction_type'] == 'like'}

    #Users the current user follows
    followed_users = {f[1] for f in follows if f[0] == user_id}

    #Score posts
    post_scores = {}
    for post in posts:
        score = 0
        if post['id'] in positive_posts:
            score += 2  # user liked it
        if post['user_id'] in followed_users:
            score += 1  # user follows the author
        if score > 0:
            post_scores[post['id']] = score

    #Recommend top 5 posts
    recommended_posts = sorted(post_scores, key=post_scores.get, reverse=True)[:5]
    return recommended_posts
