def encrypt(text, rot):
    """ uses a caesar cipher with the text and rotation
    passed and returns cipher
    """
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted

def alphabet_position(letter):
    """ return zero-based position of letter
    """
    if letter.isupper():return ord(letter) - 65
    elif letter.islower():return ord(letter) - 97
    else:return -1

def rotate_character(char, rot):
    """ rotate char forward by rot
    """
    new_ord = alphabet_position(char) + (rot % 26)

    if new_ord > 25:
        new_ord -= 26
    elif new_ord < 0:
        new_ord += 26

    if char.isupper():return chr(new_ord + 65)
    elif char.islower():return chr(new_ord + 97)
    else: return char
