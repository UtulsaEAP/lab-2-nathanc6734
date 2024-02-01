'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    price_change = current_price - last_month_price
    mortgage = (current_price * 0.051) / 12
    print("This house is $" + str(current_price) + ". The change is $" + str(price_change) + " since last month." + 
          "\n" + "The estimated monthly mortgage is $" + f'{mortgage:.2f}' + ".")
if __name__ == "__main__":
    real_estate()