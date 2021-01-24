# Advent of Code Day 25


def transform(subject, loop_size):
    value = 1
    for i in range(loop_size):
        value = value * subject
        value = value % 20201227
    return value


def decrypt(public):
    val = 1
    subj = 7
    loop = 0
    while val != public:
        val = val * subj
        val = val % 20201227
        loop += 1
    return loop


with open('input/day25.txt', 'r') as f:
    data =  f.read().split('\n')
    card_key = int(data[0])
    door_key = int(data[1])


card_loop = decrypt(card_key)
door_loop = decrypt(door_key)


print(f'Encryption Key (Card decrypted): {transform(door_key, card_loop)}')
print(f'Encryption Key (Door decrypted): {transform(card_key, door_loop)}')
