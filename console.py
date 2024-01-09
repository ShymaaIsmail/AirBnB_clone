#!/usr/bin/python3
"""Setting console for AirBnB project"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Setting methods and attributes for main console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "quit command to exit the program"
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        "dealing with an empty lines"
        pass

    def help_quit(self):
        """help for quit command"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """help for EOF"""
        print()

    def default(self, arg):
        print(f"Unknown command: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
