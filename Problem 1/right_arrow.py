'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    ''' Type your code here. '''
    row2 = 6*base_char + 2*head_char
    row3 = 6*base_char + 3*head_char

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()