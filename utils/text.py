import random


def get_word_list():
    with open('config/oxford', mode='r', encoding="utf8") as txt:
        lines = txt.readlines()
        result = [s for s in lines if len(s) >= 5]

    return result


def build_string():
    words = get_word_list()

    verb_ = ''
    noun_ = ''
    adj_ = ''

    random.seed()
    while not (adj_ and noun_ and verb_):
        rand_i = random.randrange(len(words) - 1)
        tokens = words[rand_i].split(' ')
        if adj_ and noun_ and verb_:
            break
        elif not adj_ and 'adj.' in tokens[:5]:
            adj_ = tokens[0]
        elif not noun_ and 'n.' in tokens[:5]:
            noun_ = tokens[0]
        elif not verb_ and 'v.' in tokens[:5]:
            verb_ = tokens[0]
        else:
            continue

    pool = [str(random.randrange(1001, 9999)), adj_, noun_]
    if random.randrange(2, 4) == 3:
        pool.append(verb_)

    random.shuffle(pool)

    return ''.join(pool)
