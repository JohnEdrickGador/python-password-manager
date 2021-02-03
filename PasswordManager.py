import time
import os

class MasterAccount():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.accounts = {}
        text = open(f"{self.username}.txt","a")
        text.close()
        source = open(f"{self.username}.txt","rt")
        lines = source.readlines()
        for line in lines:
            line = line.rstrip()
            line = line.split(":")
            self.accounts[line[0]] = line[1]
        source.close()
    def addAccount(self):
        print("Add an account")
        account = input("Enter account (e.g. example@gmail.com): ")
        password = input("Enter password: ")
        if account in self.accounts:
            print("account already exists")
        else:
            self.source = open(f"{self.username}.txt","a")
            self.accounts[account] = password
            line = account + ":" + password + "\n"
            self.source.write(line)
            self.source.close()
    def viewAccounts(self):
        if len(self.accounts) == 0:
            print("There are no saved accounts")
        else:
            print("============= Accounts =============\n")
            for key in self.accounts.keys():
                print(f"account: {key} password: {self.accounts[key]}")
def login(username_input,password_input):
    global accounts
    if username_input in accounts:
        if accounts[username_input] == password_input:
            return True
        else:
            return False
    else:
        return False
def clear():
    os.system('cls')

if __name__ == "__main__":
    doc = open("users.txt","rt")
    lines = doc.readlines() 
    details = []
    for line in lines:
        line = line.rstrip()
        details.append(line)
    accounts = {}
    for data in details:
        data = data.split("/")
        for i in data:
            i = i.split(":")
            accounts[i[0]] = i[1]
    doc.close()
    #signup or login
    print("Welcome to JEG's password manager v1.1")
    choice = int(input("[1] - Log In\n[2] - Sign Up\n"))
    if choice == 1:
        #login
        if len(accounts) == 0:
            print("no accounts detected")
        else:
            tries = 3
            while True:
                if tries == 0:
                    print("Sorry. You dont have attempts left")
                    time.sleep(1)
                    exit()
                else: 
                    print("Welcome to JEG's password manager v1.0")
                    username_input = input("Enter your username: ")
                    password_input = input("Enter your password: ")
                    if login(username_input,password_input):
                        clear()
                        break
                    else:
                        print("check your inputs and try again")
                        tries -= 1
                        clear()
                user = MasterAccount(username_input,password_input)
                user_input = int(input(f'''Hello {user.username}, Please select one of the following operations: \n [1] - Add an account\n [2] - View accounts\n [3] - exit\n'''))
                clear()
                if user_input == 1:
                    user.addAccount()
                    exit()
                elif user_input == 2:
                    user.viewAccounts()
                    exit()
                elif user_input == 3:
                    exit()

    elif choice == 2:
    #sign up
        while True:
            doc = open("users.txt","a")
            new_username = input("Enter desired username: ")
            new_password = input("Enter your password: ")
            if new_username in accounts.keys():
                print("Username is taken")
            else:
                line = new_username + ":" + new_password + "\n"
                doc.write(line)
                doc.close()
                new_file = open(f"{new_username}.txt","a")
                new_file.close()
                time.sleep(1)
                print("Account succesfully created")
                break
    else:
        print("invalid input. Relaunch the app")

    
