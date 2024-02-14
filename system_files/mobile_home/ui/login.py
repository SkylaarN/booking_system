from .decoration import display, tab, colours, prompt
from logic.to_database import verify_acc


def login():
    """
    use maskpass pass word for 
    """
    attempts = 3
    while attempts > 0:
        display(text="1.lOGIN", color="yellow", space=2)
        email = prompt(text="Enter your email", color="blue")
        passw = prompt(text="Enter your password.", color="blue")
        # print(passw, type(passw))
        status, user_name = verify_acc(email, passw)
        print(status, user_name)
        if status == "success":
            display(text=f"Welcome back {user_name}", color="magenta", space=3)
            return "perfom actual actions"
        else:
            attempts -= 1
            display(text=f"Wrong!!(Attemps left ={attempts}", color="red", space=3)
    