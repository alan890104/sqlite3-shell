import sqlite3,colorama,os
from colorama import Fore, Back, Style

colorama.init()
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
reset = Fore.RESET


def ListToFormattedString(alist):
    # Create a format spec for each item in the input `alist`.
    # E.g., each item will be right-adjusted, field width=3.
    # print(len(Fore.GREEN+"None"+Fore.RESET)) -> 29
    format_list = ['{:<15}'.format(item) if item!=None else '{:<25}'.format(Fore.GREEN+"None"+yellow) for item in alist ] 

    # Now join the format specs into a single string:
    # E.g., '{:>3}, {:>3}, {:>3}' if the input list has 3 items.
    s = ' '.join(format_list)

    # Now unpack the input list `alist` into the format string. Done!
    return s.format(*alist)

print(Back.WHITE+Fore.BLACK+"Enter DB name(press ENTER to use default name): "+Fore.RESET+Back.RESET,end='')
db_name = input()

if len(db_name.strip())==0:
    db_name = "DB.sqlite3"
elif db_name=='exit': 
    print('Exit should not be your db_name')
    exit(0)
try:
    con = sqlite3.connect(db_name)
except Exception as e:
    print(e)
    os.system('PAUSE')
    exit(0)

con.isolation_level = None
con.row_factory = sqlite3.Row  
cur = con.cursor()

buffer = ""

print(red+"Enter your SQL commands to execute in sqlite3.")
print("Enter a blank line or 'exit' to exit.")
print(Fore.LIGHTMAGENTA_EX+"{:<10}{:<25}".format("command","usage"))
print(Fore.LIGHTCYAN_EX+"{:<10}{:<25}".format("ls","list all tables"))
print("{:<10}{:<25}".format("help","show all commands"))
print("{:<10}{:<25}".format("<sql>","execute sql commands"))
print("{:<10}{:<25}".format("exit","leave this program")+Fore.RESET)

print(green+"---------------NEW COMMAND-----------------"+reset)
sign = '>> '
while True:
    line = input(sign)
    if line == "" or line.strip()=='exit':
        reset
        break
    if line.strip()=="ls" and buffer=="":
        line = "SELECT SQL FROM sqlite_master WHERE type='table';"
    elif line.strip()=="help" and buffer=="":
        print(Fore.LIGHTMAGENTA_EX+"{:<10}{:<25}".format("command","usage"))
        print(Fore.LIGHTCYAN_EX+"{:<10}{:<25}".format("ls","list all tables"))
        print("{:<10}{:<25}".format("help","show all commands"))
        print("{:<10}{:<25}".format("<sql>","execute sql commands"))
        print("{:<10}{:<25}".format("exit","leave this program")+Fore.RESET)
        continue
    elif line.strip()[-1]!=';':
        sign = '...  '
    else:
        sign = '>> '
        reset
    buffer += ' '+line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)
            if buffer.lstrip().upper().startswith("SELECT"):
                print(yellow,end='')
                ret = cur.fetchall()
                if len(ret)>0:
                    col_name = ret[0].keys()
                    print(ListToFormattedString(col_name).upper())
                    for x in ret:
                        print(ListToFormattedString(dict(x).values()))
                    # print(ListToFormattedString(ret.values()))
                print(reset,end='')
        except sqlite3.Error as e:
            print(red+"An error occurred:"+' '+e.args[0]+reset)
            print(green+"---------------NEW COMMAND-----------------"+reset)
        except Exception as e:
            print(red+"ERROR: "+str(e)+reset)
            print(green+"---------------NEW COMMAND-----------------"+reset)
        buffer = ""

con.close()