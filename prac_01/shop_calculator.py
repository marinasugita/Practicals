total_price = 0
number_of_items = int(input('Enter number of items: '))
while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input('Enter number of items: '))
for i in range(0, number_of_items, 1):
    item_price = int(input('Price of item: '))
    total_price += item_price
if total_price > 100:
    discount_price = total_price - (total_price * 0.1)
    print('Total price for {} items is {}'.format(number_of_items, discount_price))
else:
    print('Total price for {} items is {}'.format(number_of_items, total_price))
