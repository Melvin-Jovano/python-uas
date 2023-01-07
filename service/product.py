from models.Product import Product
from database import product as productDatabase
from database import productType as productTypeDatabase
from utilsFolder.text_style import TextStyle
import os

def product():
    while True:
        os.system('clear||cls')
        print('0. Back')
        print('1. Add Product')
        print('2. Edit Product')
        print('3. Delete Product')
        print('4. List All Product')
        print('5. Restock Product')

        choice = input('\nEnter Option: ')

        if choice == '0': break

        if choice == '5':
            while True:
                # Check If Theres At Least 1 Product Available
                if len(productDatabase) == 0: 
                    print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                while True:
                    try:
                        n = 1
                        os.system('clear||cls')
                        print('0. Exit')
                        for p in productDatabase:
                            print(f'{n}. {p.name}')
                            n += 1
                        product = int(input('\nChoose Product: '))
                        break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                try:
                    if not(0 <= product <= n-1): raise Exception
                    if product == 0: break

                    while True:
                        try:
                            os.system('clear||cls')
                            print(f'Stock: {productDatabase[product-1].stock}')
                            stock = int(input('\nStock: '))
                            break
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                            input('\nPress Enter...')

                    productDatabase[product-1].stock = stock

                    os.system('clear||cls')
                    print(f'{TextStyle.GREEN}Product Restocked{TextStyle.END}')
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number Between 0 - {n-1}{TextStyle.END}')
                    input('\nPress Enter...')

        if choice == '1':
            # Check If Theres At Least 1 Product Type Available
            if len(productTypeDatabase) == 0: 
                os.system('clear||cls')
                print(f'{TextStyle.RED}No Product Types Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break

            os.system('clear||cls')
            name = input('Name: ')

            while True:
                try:
                    os.system('clear||cls')
                    price = int(input('Price: Rp.'))
                    break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')

            while True:
                try:
                    os.system('clear||cls')
                    stock = int(input('Stock: '))
                    break
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')

            while True:
                try:
                    os.system('clear||cls')
                    n = 1
                    for p in productTypeDatabase:
                        print(f'{n}. {p.name}')
                        n += 1
                    productType = int(input('\nProduct Type: '))
                    if 1 <= productType < n:
                        break
                    else:
                        os.system('clear||cls')
                        print(f'{TextStyle.RED}Please Input Number Between 1 - {n-1}{TextStyle.END}')
                        input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                    input('\nPress Enter...')

            productDatabase.append(Product(name, price, stock, productTypeDatabase[productType-1]._id))

            os.system('clear||cls')
            print(f'{TextStyle.GREEN}Product Added{TextStyle.END}')
            input('\nPress Enter...')

        if choice == '2':
            while True:
                # Check If Theres At Least 1 Product Available
                if len(productDatabase) == 0: 
                    print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                while True:
                    try:
                        n = 1
                        os.system('clear||cls')
                        print('0. Exit')
                        for p in productDatabase:
                            print(f'{n}. {p.name}')
                            n += 1
                        product = int(input('\nChoose Product: '))
                        break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                try:
                    if not(0 <= product <= n-1): raise Exception
                    if product == 0: break

                    os.system('clear||cls')
                    print(f'Name: {productDatabase[product-1].name}')

                    name = input('\nName: ')
                    while True:
                        try:
                            os.system('clear||cls')
                            print(f'Price: Rp.{productDatabase[product-1].price}')
                            price = int(input('\nPrice: Rp.'))
                            break
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                            input('\nPress Enter...')

                    while True:
                        try:
                            os.system('clear||cls')
                            print(f'Stock: {productDatabase[product-1].stock}')
                            stock = int(input('\nStock: '))
                            break
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                            input('\nPress Enter...')

                    while True:
                        try:
                            n = 1
                            os.system('clear||cls')
                            for pt in productTypeDatabase:
                                if pt._id == productDatabase[product-1].productTypeId:
                                    print(f'Type: {pt.name}\n')

                            for p in productTypeDatabase:
                                print(f'{n}. {p.name}')
                                n += 1
                                
                            productType = int(input('\nProduct Type: '))
                            if 1 <= productType < n:
                                break
                            else:
                                os.system('clear||cls')
                                print(f'{TextStyle.RED}Please Input Number Between 1 - {n-1}{TextStyle.END}')
                                input('\nPress Enter...')
                        except:
                            os.system('clear||cls')
                            print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                            input('\nPress Enter...')

                    productDatabase[product-1].price = price
                    productDatabase[product-1].name = name
                    productDatabase[product-1].stock = stock
                    productDatabase[product-1].productTypeId = productTypeDatabase[productType-1]._id

                    os.system('clear||cls')
                    print(f'{TextStyle.GREEN}Product Updated{TextStyle.END}')
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Please Input Number Between 0 - {n-1}{TextStyle.END}')
                    input('\nPress Enter...')

        if choice == '3':
            while True:
                # Check If Theres At Least 1 Product Available
                if len(productDatabase) == 0: 
                    print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
                    input('\nPress Enter...')
                    break

                while True:
                    try:
                        n = 1
                        os.system('clear||cls')
                        print('0. Exit')
                        for p in productDatabase:
                            print(f'{n}. {p.name}')
                            n += 1
                        product = int(input('\nChoose Product: '))
                        break
                    except:
                        os.system('clear||cls')
                        print(f"{TextStyle.RED}Input Must Be a Number{TextStyle.END}")
                        input('\nPress Enter...')

                try:
                    if not(0 <= product <= n-1): raise Exception
                    if product == 0: break

                    productDatabase.pop(product-1)

                    os.system('clear||cls')
                    print(f'{TextStyle.RED}Product Deleted{TextStyle.END}')
                    input('\nPress Enter...')
                except:
                    os.system('clear||cls')
                    print(f"{TextStyle.RED}Please Input Number Between 0 - {n-1}{TextStyle.END}")
                    input('\nPress Enter...')

        if choice == '4':
            # Check If Theres At Least 1 Product Available
            if len(productDatabase) == 0: 
                print(f'{TextStyle.RED}No Products Were Found, Please Create A New One...{TextStyle.END}')
                input('\nPress Enter...')
                break

            n = 1
            os.system('clear||cls')
            for p in productDatabase:
                print(f'{n}. {p.name}, Stock: ', end='')
                if p.stock == 0:
                    print(f'{TextStyle.RED}{p.stock}{TextStyle.END}')
                else:
                    print(f'{TextStyle.GREEN}{p.stock}{TextStyle.END}')
                n += 1

            input('\nPress Enter...')
