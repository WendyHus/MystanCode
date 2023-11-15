"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Give a secret number and this program will decipher the confidential information.
    """
    number = int(input('Secret number: '))
    string = str(input("What's the ciphered string?")).upper()
    new_alphabet = ALPHABET[26-number % 26:] + ALPHABET[:26-number % 26]
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        index = new_alphabet.find(string[i])
        if index != -1:               # if string exists in new_alphabet.
            ans += ALPHABET[index]   # Get the corresponding letter through the same loop number.
        else:
            if not string[i].isalpha():   # If it is not a letter, no need to modify and replace it.
                ans += ch
    print('The deciphered string is: ' + ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
