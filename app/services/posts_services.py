def creating_id(list_posts: list):
    
    if (len(list_posts) == 0):
        return 1

    length_list = len(list_posts)
    last_post = list_posts[length_list - 1]

    if (last_post["id"] > length_list or last_post["id"] == length_list):
        return last_post["id"] + 1
        
    else: 
        return length_list

