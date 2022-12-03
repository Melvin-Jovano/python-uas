from service.animal import animal

while True:
    print('0. Exit')
    print('1. Animal Database')
    choice = input('Enter Option: ')

    if choice == '0': break

    if choice == '1':
        animal()