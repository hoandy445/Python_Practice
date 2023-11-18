try: 
    balance = float(input("Enter your starting balance: $"))
    apy = float(input("Enter APY: %"))
    addbalance = float(input("Enter the amount you'll be adding to this account per year: $"))
    years = float(input("Enter the amount of years: "))

    if balance < 0 or apy < 0 or addbalance < 0 or years < 0:
        quit()

except:
    print("Calculations cannot be made. Inputs must be numbers and cannot be negative.")
    print("Closing program...")
    quit()

apy = apy / 100
total_interest = 0
counter = 0


while counter < years:
    interest = balance * apy
    balance = balance + interest
    total_interest = total_interest + interest
    counter = counter + 1
    balance = balance + addbalance


print("after", round(years), "years:")
print("balance: $", round(balance, 2))
print("total interest earned: $", round(total_interest, 2))
