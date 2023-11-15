"""
File: name_sq.py (extension)
Name: 
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    """
    print(name_diamond('JERRY'))

def name_diamond(name):
    name_upper = name.upper()
    name_length = len(name_upper)
    for i in range(1, name_length+1):
        print(name_upper[:i])
    for i in range(1, name_length):
        print(i*' ' + name_upper[i:])

    for i in range(len(name)):
        print(name[0:1+i])
    for j in range(len(name)-1):
        for k in range(1+j):
        print(‘ ‘,end=“”)
        print(name[j+1:])


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
