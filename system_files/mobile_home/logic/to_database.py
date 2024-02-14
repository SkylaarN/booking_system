
#my own imports


#builtin imports
import json
from pathlib import Path


def new_user(passw = "", email = "", user_name=""):
    new_user_dict = {
            "user_name" : user_name,
            "email" : email,
            "password" : passw,
            "events" : {
                "listings" : "empty",
                "bookings" : "empty"
                }    
            }
    
    return new_acc(new_user_dict)

path = Path("accounts.json")
def new_acc(new_user_dict):
    # path = Path("..accounts.json")
    with open(path, "r") as save_acc:
        file_data = json.load(save_acc)

    with open(path, "w") as save_acc:
        old_data = file_data["saved_accounts"]
        new_data = old_data+[new_user_dict]
        save_data = json.dump({"saved_accounts":new_data}, save_acc, indent=2)

    return 

def verify_acc(email="", passw=""):

    with open(path, "r") as save_acc:
        file_data = json.load(save_acc)
    
    for user in file_data["saved_accounts"]:
        if user["email"] == email and user["password"] == passw:
            print(user["user_name"])
            return "success", user["user_name"]
    return "ll"
    
print(verify_acc(email="12", passw="123"))