'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    area_code = phone_number // 10000000
    prefix = (phone_number %10000000) // 10000
    line_number = phone_number % 10000
    print("(" + str(area_code) + ") " + str(prefix) + "-" + str(line_number))
if __name__ == "__main__":
    telephone()