# from ui.decoration import display, tab, colours, txt, star
# from ui.login import login
# from ui.create_acc import create_account

# def sys_control():
#     display(space=1, color="blue", stars=45)
#     display(color="yellow", text="Welcome to Mobile HOME!" ,space=2 )
#     display(space=1, color="blue", stars=45)
#     display(color="yellow", text="MENU!" ,space=3)
#     for item in ["1.Login", "2.Create Account"]:
#         display(color="blue", text=item ,space=2)

#     text = tab(2)+colours("blue")+" >> "+colours("reset")
#     while True:
#         choice = input(text)
#         display(space=1, color="blue", stars=45)
#         if choice == "1" or choice.lower() == "login":
#             return login()
#         elif choice == "2" or choice.lower() == "create_acc":
#             return create_account()
#         display(space=2, color="yellow", text="Enter a valid choice")


# def logged_in(username=""):
#     welcome_txt = colours(colour="yellow")+tab(2)+"Welcome "+colours("magenta")+username+colours("reset")
#     print(welcome_txt)


# if __name__ == "__main__":
#     sys_control()
#     logged_in("Nathi")