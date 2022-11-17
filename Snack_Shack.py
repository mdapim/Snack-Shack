
import datetime

snacks_available = [{"item": 'Sandwich','prep':  60,'serve': 30, 'amount': 45},
                    {"item": 'Potato', 'prep': 150,'top': 30,'serve': 30 }]

def ask_for_order():
    order = input('What would you like to order today?,')
    if(order == '1'):
        return 'Sandwich'
    elif(order == 'submit'):
        return 'S'
    else:
        return 'None'
    
def print_order_sequence(orders):
    sequence_order_time = 0
    print('Chefs sequence of orders')
    print(f'{len(orders)} Sandwiches ordered')
    for i in range(len(orders)):
        print(f'{turn_seconds_to_min(sequence_order_time)} start making sandwich {i + 1}')
        sequence_order_time += snacks_available[0]["prep"]
        print(f'{turn_seconds_to_min(sequence_order_time)} serve sandwich {i + 1}')
        sequence_order_time += snacks_available[0]["serve"]

def print_order_estimation(orders):
    print('\n\n\n\n------------------------------------------')
    print('Customers Order times')
    order_time = 0
    for i in range(len(orders)):
        order_time += snacks_available[0]["prep"] + snacks_available[0]["serve"]
        print(f'Customer {i+1} order of {orders[i]} will be done in {turn_seconds_to_min(order_time)}')


def turn_seconds_to_min(seconds):
    return str(datetime.timedelta(seconds=seconds))

def check_order_return_time(order_list):
    estimated_order_time = 0
    return_num = 0
    for i in range(len(order_list)):
        estimated_order_time += snacks_available[0]["prep"] + snacks_available[0]['serve']
        print(estimated_order_time)
        if(estimated_order_time > 300):
            return_num = i

    return return_num


def main():
    print('Controls:')
    print('1 to order sandwich')
    print('q to exit')
    print('submit to move to next batch of orders')
    order_list = []
    taking_orders = True
    while(taking_orders):
        returned_order = ask_for_order()
        if(returned_order == 'None'):
            taking_orders = False
        elif(returned_order == 'S'):
            snacks_available[0]["amount"] -= len(order_list)
            order_list.clear()
        else:
            order_list.append(returned_order)
            if(check_order_return_time(order_list) == 0):
                print_order_sequence(order_list)
                print_order_estimation(order_list)
                print('Sandwiches available: ', snacks_available[0]['amount'])
            else:
                order_list.pop()
                print('Sorry we are unable to get your order to you within 5 minutes')

        

    





main()