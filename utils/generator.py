
def build_string():
    return 'raw_string'


def generate_hashed_pword():
    raw_string = build_string()
    return hash(raw_string)


def hash(raw_string):
    return 'generated_hash'


def unhash(hashed_string):
    return 'unhashed_string'
