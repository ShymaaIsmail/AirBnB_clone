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
from models import storage

classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]


class HBNBCommand(cmd.Cmd):
    """Setting methods and attributes for main console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "quit command to exit the program"
        return True

    def do_EOF(self, arg):
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
        else:
            instant_id = eval(args[0])()
            instant_id.save()
            print(instant_id)

    def do_show(self, arg):
        """Showing instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instant_id = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if instant_id in objects:
                print(objects[instant_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy instance of class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instant_id = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if instant_id in objects:
                del objects[instant_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Printing all instance of class"""
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            for obj in objects.values():
                print(obj)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key in objects:
                if key.startswith(args[0]):
                    print(objects[key])

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
        else:
            obj_id = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if obj_id in objects:
                obj = objects[obj_id]
                att_name = args[2]
                att_value = args[3].strip('"')
                if hasattr(obj, att_name):
                    att_type = type(getattr(obj, att_name))
                    setattr(obj, att_name, att_type(att_value))
                    obj.save()
            else:
                print("** no instance found **")

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
