# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#1st program
if __name__ == '__main__':
    z = 9
    o = 0.5
    v = 5
    print("1st program:", (z**o)*v)

#2nd program
if __name__ == '__main__':
    z = 9.99
    o = 9.98
    v = 1000
    x = 1000.1
    print("2nd program:",z>o and v!=x)

#3d program
if __name__ == '__main__':
    z = 2
    print("3d program:", z*z+z==z*(z+z))

#4th program
if __name__ == '__main__':
    str_z = '123.456'
    v = (float(str_z)*10)%10
    print("4th program:", int(v))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/