'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''
    
    product = num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4) / 4

    print(f'{product:.0f}' + " " + f'{average:.0f}' + 
          "\n" + f'{product:.3f}' + " " + f'{average:.3f}')
if __name__ == "__main__":
    simple_stats()