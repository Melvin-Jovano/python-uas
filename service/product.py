from models.Product import Product
from database import product as productDatabase
from database import productType as productTypeDatabase
import os

def product():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Poduct')
        print('2. Edit Poduct')
        print('3. Delete Poduct')

        choice = input('Enter Option: ')

        if choice == '0': break

        if choice == '1':
            os.system('clear||cls')

            # Check If Theres At Least 1 Product Type Available
            if len(productTypeDatabase) == 0: 
                print('No Product Type Were Found, Please Create A New One...')
                input('Press Enter...')
                break

            name = input('Name: ')

            while True:
                try:
                    price = input('Price: Rp.')
                    break
                except:
                    print("Input Must Be a Number")

            while True:
                try:
                    stock = input('Stock: ')
                    break
                except:
                    print("Input Must Be a Number")
            
            n = 1

            for p in productTypeDatabase:
                print(f'{n}. {p.name}')
                n += 1

            while True:
                try:
                    productType = int(input('Product Type: '))
                    break
                except:
                    print("Input Must Be a Number")

            productDatabase.append(Product(name, price, stock, productTypeDatabase[productType-1]._id))

            print('Product Added')
            input('Press Enter...')

        if choice == '2':
            while True:
                os.system('clear||cls')
                # Check If Theres At Least 1 Product Available
                if len(productDatabase) == 0: 
                    print('No Product Were Found, Please Create A New One...')
                    input('Press Enter...')
                    break
                
                n = 1

                print('0. Exit')
                for p in productDatabase:
                    print(f'{n}. {p.name}')
                    n += 1

                while True:
                    try:
                        product = int(input('Choose Product: '))
                        break
                    except:
                        print("Input Must Be a Number")

                try:
                    if not(0 <= product <= n-1): raise Exception
                    if product == 0: break

                    print(productDatabase[product-1].name)
                except:
                    print(f'Please Input Number Between 0 - {n-1}')
                    input('Press Enter...')