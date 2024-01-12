#!/usr/bin/python3
"""Setting console for AirBnB project"""


import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
objects = storage.all()


class HBNBCommand(cmd.Cmd):
    """Setting methods and attributes for main console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "quit command to exit the program"
        return True

    def do_EOF(self, arg):
        """CTRL_C to Exit"""
        return True

    def emptyline(self):
        "dealing with an empty lines"
        pass

    def do_create(self, arg):
        """Creating instance of class"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                instant_id = eval(arg)()
                instant_id.save()
                print(instant_id.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Showing instance of class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instant_id = args[1]
                key = "{}.{}".format(class_name, instant_id)
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy instance of class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instant_id = args[1]
                key = "{}.{}".format(class_name, instant_id)
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Printing all instance of class"""
        if not arg:
            print([str(value) for value in objects.values()])
        else:
            class_name = arg.split()[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                filtered_objects = [str(value) for key, value in objects.items() if key.split(".")[0] == class_name]
                print(filtered_objects)

    def do_update(self, arg):
        """Updating instance of class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instant_id = args[1]
                key = "{}.{}".format(class_name, instant_id)
                if key not in objects:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    instant = objects[key]
                    setattr(instant, attribute_name, attribute_value)
                    instant.save()

    def default(self, arg):
        print(f"Unknown command: {arg}")

    def help_quit(self):
        """help for quit command"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """help for EOF"""
        print()

        """commands: update
        """
    def help_create():
        """Create command creating a new instance"""
        print("Help command to create a new instance")
        print()

    def help_show():
        """Show command for Showing all attributes about instance"""
        print("Show command to display all attributes about instance")
        print()

    def help_destroy():
        """Destroy command for Deleting an instance"""
        print("Destroy command to delete an instance")
        print()

    def help_all():
        """All command to Display all objects"""
        print("All command to Displaying all objects")
        print()

    def help_update():
        """Update command to modify instance attributes"""
        print("Update command to modify instance attributes")
        print()


if __name__ == '__main__':
    """if not sys.stdin.isatty():
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())"""
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            HBNBCommand().onecmd(arg)

    else:
        HBNBCommand().cmdloop()
