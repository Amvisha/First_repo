bill_one = 34.34
bill_two = 12.01
bill_three = 17.42
bill_four = 4.93
final_bill = round(bill_one + bill_two + bill_three + bill_four, 2)
dollars = int(final_bill)
cents = int((final_bill-int(final_bill)) * 100)
print(f'Price {final_bill}', f'Dollars {dollars}', f'Cents {cents}', sep='\n')
