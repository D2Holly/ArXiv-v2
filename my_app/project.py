import arxiv

def get_user_input(user_input):
    if len(user_input) == 0:
        raise ValueError('empty input')
    else:
        return True


def split_user_input(user_query):
    split_user_query = str.split(user_query)
    return split_user_query


def format_user_query(user_query):
    return "%20".join(user_query)



def arxiv_connection():
    # The line being tested
    client = arxiv.Client()
    return client



format_user_query(['The', 'Moon', 'The'])