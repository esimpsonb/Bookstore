import os
import pickle
import inspect
from .user import User

class System():

    def __init__(self,system_admin):
        self.users = {"esimpson":"1"}
        system_user = self.enter_system()
        self.interface(system_user,system_admin)

    def enter_system(self):
        user_input = input("Are you registered? (Enter 'yes' or 'no'): ")
        registered = user_input.lower() == 'yes'
        if registered:
            system_user = self.login()
        else:
            system_user = self.register()
        return system_user


    def register(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        self.users[username]=password
        money = input("Enter amount of money: ")
        system_user = User(username,money)
        return system_user

    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in self.users:
                if self.users[username] == password:
                    return self.load_user(username) 

                else:
                    print("Wrong username or password, please try again")
    
    def load_user(self,username):
        file_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\Users_data\user_"+username+".plk"
        with open(file_path, 'rb') as file:
            return pickle.load(file)

        
    def change_password(self):
        if self.login():
            username = input("Enter your username: ")
            new_password = input("Enter your new password: ")
            self.users[username] = new_password
        
        else: print("Wrong password, please try again.")

    def load_user(self,username):
        directory_path = r"C:\Users\enriq\OneDrive\Desktop\Capacitacion\Python\OOP\Data\Users_data"
        loaded_file_path = os.path.join(directory_path, "user_"+username+".pkl")
        with open(loaded_file_path, "rb") as file:
            return pickle.load(file)
    
    def interface(self,system_user,system_admin):
        from .user import User

        while True:
            option = input("enter yes if you want to continue or no if you want to exit the system: ")
            option = option.lower()
            if option not in ["yes","no"]:
                print("Invalid answer, please try again")
            else:
                if option == "yes":

                    method_string = input("What would you like to do? type options to list them: ")

                    try: 
                        method = getattr(system_user, method_string)
                        args = inspect.getfullargspec(method).args
                        args.remove("self")
                        input_args = []
                        for arg in args:
                            if arg == "store":
                                input_arg = system_admin
                            else:
                                input_arg = input("enter "+arg+": ")
                            input_args.append(input_arg)
                        method(*input_args)
                        

                    except:
                        print("Invalid method, you can try the method options to see all posibilities")

                else:
                    print("Thank you for visiting the store, we hope to see you again!")
                    break
