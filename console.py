#!/usr/bin/python3
"""Setting console for AirBnB project"""


import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]


class HBNBCommand(cmd.Cmd):
    """Setting methods and attributes for main console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "quit command to exit the program"
        return True

    def do_EOF(self, arg):
        """CTRL+C command"""
        print()
        return True

    def emptyline(self):
        "dealing with an empty lines"
        pass

    def do_create(self, arg):
        """Creating instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Showing instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Destroy instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")

    def do_all(self, arg):
        """Printing all instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updating instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")

    def default(self, arg):
        print(f"Unknown command: {arg}")

    def help_quit(self):
        """help for quit command"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """help for EOF"""
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
