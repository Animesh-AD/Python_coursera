menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}
def calculate_subtotal(order):
    subtotal = 0
    for item in order:
        subtotal += float(item['price'])
    return round(subtotal ,2)
def calculate_tax(subtotal):
    tax = (subtotal * 18) /100
    return print('your tax is : ',tax)


    

def sumarize_order(order):
    subtotal = 0
    for item in order:
        subtotal  += float(item['price'])
    total = (subtotal * 118) /100
    print('Your total bill is :',total)
    return round(total, 2), subtotal


def print_order(order):
    print('you have orderd ' + str(len(order)) + ' items')
    items = []
    items = [item['name'] for item in order]
    print(items)
    return order


def display_menu():
    print ('......menu......')
    for selection in menu:
        print(f"{selection}.{menu[selection]['name'] : <15} | {menu[selection]['price'] :>5}") 

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('select your food number ' + str(count) + '(form 1 to 5 : ) ')
        count += 1
        order.append(menu[int(item)])
    return order
    

def main():
    order= take_order()
    print_order(order)
    subtotal = calculate_subtotal(order)
    print('Your subtotal amount is : ', subtotal)
    calculate_tax(subtotal)

    sumarize_order(order)

if __name__=="__main__":
    main()