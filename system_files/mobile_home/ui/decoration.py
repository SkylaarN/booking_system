def tab(num=1):
    return "\t"*num

def star(num=1):
    return "*" * num

def colours(colour="white"):
    # will assign colours their values in here
    colours = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red":" \033[31m",
        "green": "\033[32m",
        "yellow": '\033[33m',
        "blue": '\033[34m',
        "magenta": '\033[35m',
        "cyan": '\033[36m',
        "white": '\033[37m'
    }
    chosen_colour = colours[colour]

    return chosen_colour

def prompt(num, color):
    txt = tab(num)+colours(color)+">> "+colours("reset")
    return txt


def txt(text = ""):
    return text


def display(color="", space=0, text="", stars=0):
    color = colours(color)
    space = tab(space)
    reset = colours("reset")
    text = txt(text)
    if stars > 0:
        stars = star(stars)
        return print(color,space,stars,reset)
    else:
        return print(color,space,text,reset)
    

def prompt(text="", color="white"):
    color = colours(color)
    return input(f"\033{color}\t\t{text}\n\t\t>> \033[0m")