import collections, functools, operator
from prettytable import PrettyTable
from collections import Counter
import time
from validations import get_valid_value, get_non_empty_value, get_date, get_confirmation, get_item
from database import mycollection
from aux import sales_list, sellers


#count sellers names ocurrencies
def count_names(array):
    nameArray = []
    for i in array:
        nameArray.append(i['seller_name'])

    return nameArray
    

#sales Ranking by Amount of Sales
def output_sales_ranking(list):
    new_list = []
    for i in list:
        new_list.append(
            {
                i['seller_name']: round(i['price'], 2)
            }
        )

    result = dict(functools.reduce(operator.add,
         map(collections.Counter, new_list)))

    sort_orders = sorted(result.items(), key=lambda x: x[1], reverse=True)

    sellers_names = count_names(list)

    number_sales = Counter(sellers_names)

    table = PrettyTable()
    table.field_names = ["Ranking", "Seller", "Total Sales", "Total Value($)"]

    for i in range(len(sort_orders)):
        table.add_row([i+1, sort_orders[i][0], number_sales[sort_orders[i][0]], round(sort_orders[i][1], 2)])

    print('\nSales Ranking\n')
    print(table)
    time.sleep(2)


#show all registered sales
def output_all_sales(list):
    table = PrettyTable()
    table.field_names = ["id", "Seller", "Customer", "Date", "Item sold", "Price($)"]
    index = 1
    for i in list:
        table.add_row([index, i['seller_name'], i['customer_name'], i['sale_date'], i['item_name'], i['price']])
        index += 1

    print('\nAll time sales:\n')
    print(table)
    time.sleep(2)


#edit an old item
def edit_item(list):
    output_all_sales(list)
    edit_sale = get_item('\nWhich item would you like to edit/remove? (type a number of id)\n', list)
    index = int(edit_sale)-1
    table = PrettyTable()
    table.field_names = ["id", "Seller", "Customer", "Date", "Item sold", "Price($)"]
    table.add_row([int(edit_sale), list[index]['seller_name'], list[index]['customer_name'], list[index]['sale_date'], list[index]['item_name'], list[index]['price']])
    print(table)
    confirm = get_confirmation('\nIs this the item you want to edit/remove? (Y/N)\n')
    if confirm.upper() == 'N':
        return edit_item(list)

    elif confirm.upper() == 'Y':
        options = ['1', '2']
        while True:
            seller_option = input('\n\nDo you want to edit or remove this item? (type a number)\n\n 1. Edit\n 2. Remove\n\n')
            if seller_option not in options:
                print('\nPlease select of one the options (type a number).\nYour input was: ' +  seller_option)
            elif seller_option == '1':
                add_sale(index)
                break
            else:
                confirm_again = get_confirmation('\nAre you sure you want to remove this? (Y/N)\n')
                if confirm_again.upper() == 'Y':
                    mycollection.delete_one(list[index])
                    list.pop(index)
                    print('\nSale deleted successfully! :)')
                    break
                else:
                    return edit_item(list)


#add sale or edit an old one
def add_sale(index):
    options = ['1', '2', '3', '4', '5']
    while True:
        seller_option = input('\n\nWhat is the seller name? (type a number)\n\n 1. ' + sellers[0] +'\n 2. ' + sellers[1] +'\n 3. ' + sellers[2] +'\n 4. ' + sellers[3] +'\n 5. ' + sellers[4] + '\n\n')
        if seller_option not in options:
            print('\nPlease select of one the registered sellers (type a numbe).\nYour input was: ' +  seller_option)
        else:
            customer = get_non_empty_value('\nCustomer name: \n')
            date = get_date('\nSell date (format: YYYY-MM-DD): \n')
            item = get_non_empty_value('\nSold item name: \n')
            price = get_valid_value('\nPrice sold (format: 19.99): \n')
            confirm = get_confirmation('\nYour input was: \n\ncustomer: ' + customer + '\ndate: ' + str(date) + '\nitem: ' + item + '\nprice: ' + str(price) + '\n\nConfirm? (Y/N)\n')
            
            if confirm.upper() == 'N':
                return add_sale(index)

            elif confirm.upper() == 'Y':
                seller = sellers[int(seller_option)-1]
                new_sale = {
                        'seller_name': seller,
                        'customer_name': customer,
                        'sale_date': str(date),
                        'item_name': item,
                        'price': float(price)
                    }
                if index != '':
                    mycollection.update(sales_list[index],new_sale)
                    sales_list[index] = new_sale
                    
                else:
                    mycollection.insert_one(new_sale)
                    sales_list.append(new_sale)

                output_all_sales(sales_list)
                output_sales_ranking(sales_list)
                print('\nSale registered successfully! :)')
                break



