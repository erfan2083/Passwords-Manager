def add():
    site_name = input('Site or App name = ')
    name = input('Account username = ')
    password = input('Account password = ')

    with open('passwords.txt', 'a') as f:
        f.write(site_name +
                '\nUsername = ' + name +
                '\nPassword = ' + password + '\n')


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)


while True:
    user_choice = input(
        "Would you like to add a new password or view the existing ones or change the app password (add, view, password), press Q to quit ? ")

    if user_choice == "Q":
        quit()

    if user_choice == "view":
        view()
    elif user_choice == "add":
        add()
    elif user_choice == "password":
        default_password = int(input("New app password = "))
    else:
        print('Invalid input!\n')
