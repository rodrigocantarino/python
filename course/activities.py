def eat(food, healthy):
    final1 = "because it's healthy!"
    final2 = "because we only live once!"

    if healthy:
        f = final1
    else:
        f = final2

    return f"I'm eating {food} " + f


def sleep(hours):
    if hours < 8:
        ph = "I slept a few!"
    elif 8 <= hours <= 11:
        ph = "I slept very good!"
    else:
        ph = "I slept a lot!"
    return ph


def funny(person):
    comedians = ['Jim Carrey', 'Bozo']
    if person in comedians:
        return True
    return False

