from logic.to_database import new_user
from .decoration import tab,txt,star,display,prompt

def create_account():
    display(space=3, text="2.Create Account", color="yellow")
    user_name = prompt(text="Enter your prefered name.", color="blue")
    while True:
        email = prompt(text="Enter your email", color="blue").capitalize()
        ver_email = prompt(text="Verify your email", color="blue")
        if email == ver_email:
            display(color="green", text="CORRECT!!!", space=3)
            while True: 
                passw = prompt(text="Enter your password.", color="blue")
                ver_passw = prompt(text="Verify your password.", color="blue")   
                if passw == ver_passw:
                    display(color="green", text="CORRECT!!!", space=3)
                    display(space=1, color="blue", stars=45)
                    return new_user(passw=passw, email=email)
                display(color="red", text="WRONG!!!", space=3)
        display(color="red", text="WRONG!!!", space=3)
