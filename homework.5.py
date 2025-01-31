import colorama
print(colorama.__version__)
from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + "червоний")
print(Fore.GREEN + "зелений")
print(Fore.BLUE + "синій")
print(Back.YELLOW + "жовтий фон" + Fore.BLACK)
print(Style.BRIGHT + "Жирний текст")
print(Style.DIM + "курсивний??")