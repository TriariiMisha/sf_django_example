import re


def sanitize_string(init_string):
    return re.sub(r'[\W_]+', '', init_string)
