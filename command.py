from enum import Enum
import database


class Squares(Enum):
    GREEN = '🟩'
    YELLOW = '🟨'
    BLACK = '⬛'
    WHITE = '⬜'


square_list = ['🟩', '🟨', '⬛', '⬜']


def handle_command(message):
    command = message.content.split(' ')[0]
    output = ""
    if command == 'Wordle':
        output = wordle(message)
    elif command == '!leaderboard':
        output = leaderboard()
    return output


# TODO
def leaderboard():
    # database.leaderboard()
    return 'TODO Leaderboard'


def wordle(message):
    valid = validate_command(message.content)
    if valid is not None:
        valid['author'] = message.author.name + "#" + message.author.discriminator
        valid['channel_id'] = message.channel.id
        database.put_scores(valid)
        return 'Valid'


# Make sure that the form is
def validate_command(command):
    comm = command.split("\n")
    print(comm)
    '''
    Line 0: Check the 3 components 'Wordle # #/6'
    Line 1: Empty
    Line 2 - 7: Should be comprised of 5 characters each
    '''
    # Checking #1
    line = comm[0].split(" ")
    if len(line) != 3:
        print("Wrong Length")
        return None
    if line[0] != "Wordle":
        print("not Wordle")
        return None
    if int(line[1]) < 0:
        print("Not int")
        return None
    line_1_part_3 = line[2].split("/")
    if int(line_1_part_3[0]) > 6 or int(line_1_part_3[0]) < 0:
        print("Number is too high or too low")
        return None
    # Attempts: x/6 in the first line
    attempts = int(line_1_part_3[0])
    if int(line_1_part_3[1]) != 6:
        print("Second number not false")
        return None

    # Checking #2
    if comm[1] != '\n':
        valid_line_2 = False

    # Checking #3
    if attempts != len(comm)-2:
        print("Rows don't match attempts")
        return None
    for i in range(2, len(comm)):
        # Validate if each row is 5 chars long
        if len(comm[i]) != 5:
            print("Invalid number of words in row")
            return None
        matched_list = [letters in square_list for letters in comm[i]]
        # Validate if each row consists of variables from the enum
        if all(matched_list) is not True:
            print("Unusable characters in string")
            return None
    print("We're good")
    blob = ''
    for i in range(2, len(comm)):
        blob += comm[i] + '\n'
    return {
        'day': line[1],
        'score': line_1_part_3[0],
        'blob': blob
    }
