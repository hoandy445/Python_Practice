### calculating pricing through user input ###
# allow user to input arbitrary number of prices, add the total, then apply 7% sales tax
# input should allow all prices to be entered at once, each price separated by spaces

### display receipt ###
# show "receipt", to user, which includes all prices for individual items, a subtotal (before taxes), and a final total (tax applied)

### error handling ###
# ensure program functions correctly even with improper user input

### readablity ###
# use meaningful function and variable names, and provide comments to explain the purpose of each section of code


### MODULES ###
import json
import datetime


### FUNCTIONS ###
def read_file():
    try:
        with open('receipt_file.json', 'r') as file_handle:
            receipt_file = json.load(file_handle)
            print('receipt_file.json was sucessfully opened.')
            return receipt_file

    except FileNotFoundError:
        print('receipt_file.json could not be opened. Blank file started.')
        return {}

def write_file(all_receipts):
    try:
        with open('receipt_file.json','w') as file_handle:
            json.dump(all_receipts,file_handle)
            print('Data successfully saved to "receipt_file.json".')
    except Exception as e:
        print(f'Data could not be saved to "receipt_file.json because of error "{e}".\nClosing application...')
        quit()

def get_user_input():
    return input('Please enter a selection:\n> ')

### CLASS ###
class Receipt:
    tax_rate = 1.07

    @staticmethod
    def increase_receipt_number():
        if len(receipt_file) > 0:
            for key in receipt_file:
                number_position = key[key.find('#') + 1:key.find(':')]
                last_receipt_number = int(number_position)
                return last_receipt_number + 1
        else:
            return 1000

    @classmethod
    def apply_tax(cls,subtotal_price):
        return round(subtotal_price*cls.tax_rate,2)

    @staticmethod
    def get_prices():
        prices = []
        
        while True:
            user_input = input('Enter all prices separated by spaces (example: 32.50 22.00).\n> ').strip()
            
            try:
                user_input = user_input.split()
                for price in user_input:
                    price = round(float(price),2)
                    prices.append(price)
                return prices
            except ValueError:
                print('Invalid input. Only numbers and decimals can be entered. Please try again.')
                input('Press "Enter" to re-enter prices...')
                continue

    @staticmethod
    def get_subtotal(prices):
        return round(sum(prices),2)
    
    @classmethod
    def get_receipt_name(cls):
        receipt_name = f'Receipt #{cls.increase_receipt_number}: {today}'
        return receipt_name

    @staticmethod
    def display_receipt(item_prices,subtotal_price,total_price):
        item_counter = 0
        for price in item_prices:
            item_counter += 1
            print(f'Item #{item_counter}: ${round(price,2)}')    

        print(f'''
Subtotal: ${subtotal_price}
Total: ${total_price}      ''')
        

### MAIN PROGRAM ###
# open and read file receipt file
receipt_file = read_file()


# receipt data logging info
today = datetime.date.today() 
receipt_name = Receipt.get_receipt_name()

# store prices and totals in variables
item_prices = Receipt.get_prices()
subtotal_price = Receipt.get_subtotal(item_prices)
total_price = Receipt.apply_tax(subtotal_price)
receipt_info = {
    'Item prices':item_prices,
    'Subtotal':subtotal_price,
    'Total':total_price}

# show receipt to user
print(receipt_name)
Receipt.display_receipt(item_prices,subtotal_price,total_price)

Receipt.increase_receipt_number()

# dump data into receipt .json file
if receipt_file:
    all_receipts = receipt_file
else:
    all_receipts = {}

all_receipts[receipt_name] = receipt_info
write_file(all_receipts)
