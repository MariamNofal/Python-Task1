import logparser_module
import linkparser_module
import monitor_module
# import atdetect_module
import scanner_module

modules = [logparser_module, monitor_module, scanner_module, linkparser_module]
def show_modules_screen():
    print("")
    print("To Choose from available modules enter number")
    print("1 for log parser")
    print("2 for Directory monitoring")
    print("3 for ports scanner")
    print("4 for link parser")
    print("5 for Attack detection")

    print("each feature has its own arguments use 1 -h to show help for this feature")
    print("use -o filename to redirect to this file")
    print("ex: 1 ~/test -o out.txt")
    print("Press any key to print this main list")
    print("")


if __name__ == "__main__":
    show_modules_screen()
    while 1:
        cmd = raw_input(">")
        if (len(cmd) < 1):
            show_modules_screen()
            continue

        try:
            id = int(cmd[0])
        except ValueError:
            print("Wrong format")
            show_modules_screen()
            continue
        
        if id > 5 or id < 1 :
            print("Wrong id number")
            continue
        
        if cmd.find("-h") > 0:
            modules[id - 1].help()
            continue
        print(cmd[2:])
        modules[id - 1].run(cmd[2:])
