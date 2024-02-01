'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    six_hours = caffeine_mg / 2
    twelve_hours = caffeine_mg / 4
    twenty_four_hours = caffeine_mg / 16
    print("After 6 hours: " + f'{six_hours:.2f}' + " mg" + 
          "\n" + "After 12 hours: " + f'{twelve_hours:.2f}' + " mg" + 
          "\n" + "After 24 hours: " + f'{twenty_four_hours:.2f}' + " mg")
if __name__ == "__main__":
    caffeine()