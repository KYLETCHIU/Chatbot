import random


def random_string():
    random_list = [
        "I am still studying that topic. Please email kyle.t.chiu@homedepot.com for a quick and appropriate answer. Your questions help me learn.",
        "Oh! It appears you wrote something I don't understand yet. Please email kyle.t.chiu@homedepot.com for a quick and appropriate answer. Your questions help me learn.",
        "Do you mind trying to rephrase that? Or, email kyle.t.chiu@homedepot.com for a quick and appropriate answer to your question. Your questions help me learn.",
        "I can't answer that yet. Please email kyle.t.chiu@homedepot.com for a quick and appropriate answer to your question. Your questions help me learn."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]