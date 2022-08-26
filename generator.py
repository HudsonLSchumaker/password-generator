
import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'w', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z']


def generate():
    global letters
    first = ""
    for x in range(5):
        first += letters[random.randint(0, 25)]

    first += str(random.randint(0, 9))

    second = ""
    for y in range(6):
        if y == 4:
            second += letters[random.randint(0, 25)].upper()
        else:
            second += letters[random.randint(0, 25)]

    third = ""
    for z in range(6):
        third += letters[random.randint(0, 25)]

    print(first + "-" + second + "-" + third)


if __name__ == '__main__':
  generate()
