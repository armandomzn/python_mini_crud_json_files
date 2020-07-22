""" Manage Customers """
import os
import doctest
import re
import helpers
import json
import datetime


class Client:

    def __init__(self, name, last_name, dni):
        self.name = name
        self.last_name = last_name
        self.dni = dni


def show(customer):
    print(customer.replace('.json', ''))


def show_all():
    files = os.listdir('clients/')
    json_files = [file for file in files if file.endswith('.json')]
    for customer in json_files:
        show(customer)


def show_customer():
    customer_name = input('Name of the customer to search: ').lower().split(' ')
    try:
        with open('clients/'+'_'.join(customer_name)+'.json', 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=2))
    except FileNotFoundError:
        print('The customer doesn\'t exist')


def delete_customer():

    name_file = input(
        'Select the customer file to delete: ').lower().split(' ')
    file_name = '_'.join(name_file)
    if os.path.isfile('clients/'+file_name+'.json'):
        while True:
            sure = input(
                f'Are you sure that you want to delete the file {file_name}? y == yes | n == no: ').lower()
            if sure == 'y':
                os.remove('clients/'+file_name+'.json')
                print(f'File {file_name} successfully removed')
                break
            elif sure == 'n':
                break
    else:
        print(f'The customer file "{file_name}" doesn\'t exist')


def add_client():
    name = input('Name: ').lower()
    last_name = input('Last Name: ').lower()
    dni = input('DNI most have 2 numbers and one capitalize letter: ')

    while True:
        if is_valid(name, last_name, dni):
            break
        else:
            helpers.clear()
            print('Incorrect values')
            name = input('Name: ').lower()
            last_name = input('Last Name: ').lower()
            dni = input('DNI most have 2 numbers and one capitalize letter: ')

    customer = Client(name, last_name, dni)
    if not os.path.isfile('clients/'+customer.name+'_'+customer.last_name+'.json'):
        with open('clients/'+customer.name+'_'+customer.last_name+'.json', 'w+') as file:
            data = {
                'name': customer.name,
                'last_name': customer.last_name,
                'dni': customer.dni,
                'date': datetime.datetime.now().strftime("%H:%M:%S"),
            }
            json.dump(data, file, indent=2)
            print('Customer created Successfuly')
    else:
        print('The file already exist'.upper())


def edit_customer():
    name_edit = input('Name to edit: ').lower().split(' ')
    if customer_exist(name_edit):
        with open('clients/'+'_'.join(name_edit)+'.json', 'r') as file:
            name = input('New Name: ').lower()
            last_name = input('New Last Name: ').lower()
            dni = input(
                'New DNI most have 2 numbers and one capitalize letter: ')
            while True:
                if is_valid(name, last_name, dni):
                    break
                else:
                    helpers.clear()
                    print('Incorrect values')
                    name = input('New Name: ').lower()
                    last_name = input('New Last Name: ').lower()
                    dni = input(
                        'New DNI most have 2 numbers and one capitalize letter: ')
            data = json.load(file)

        with open('clients/'+'_'.join(name_edit)+'.json', 'w+') as file:
            data['name'] = name
            data['last_name'] = last_name
            data['dni'] = dni
            data['date'] = datetime.datetime.now().strftime("%H:%M:%S")
            json.dump(data, file, indent=2)

        os.rename('clients/'+'_'.join(name_edit)+'.json',
                  'clients/'+name+'_'+last_name+'.json')

        print('Customer edited correctly')
    else:
        print('The customer doesn\'t exist')


def is_valid(name, last_name, dni):
    '''
    >>> is_valid('Ana','Morales','999')
    False
    '''
    return len(name) > 2 and len(last_name) > 0 and re.match('[0-9]{2}[A-Z]', dni) != None


def customer_exist(name):
    return os.path.isfile('clients/'+'_'.join(name)+'.json')

# json.load(f): Load JSON data from file
# json.loads(s): Load JSON data from string
# json.dump(j,f): Write JSON object to file
# json.dumps(j): Output JSON object as string

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
