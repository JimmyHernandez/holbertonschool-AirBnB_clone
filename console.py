#!/usr/bin/python3
"""Write a program called console.py that contain the entry point of the\
    command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "city": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """It's a command line interpreter\
        that inherits from the cmd module."""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing."""
        pass

    def do_EOF(self, line):
        """Print the string "EOF" and then exits the program."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel."""
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line not in classes:
                print("** class doesn't exist **")
            else:
                str = line + "()"
                base_inst = eval(str)
                base_inst.save()
                print(base_inst.id)

    def do_show(self, line):
        """Print the value of the variable named."""

        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """It destroys the current room and all the items in it.
        """
        arg = line.split()
        obj_dict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, arg):
        """It's a function that prints all the instances of a class."""
        list_of_str = arg.split()
        obj = storage.all()

        for key in obj.keys():
            if len(list_of_str) >= 1:
                if list_of_str[0] not in classes:
                    print("** class doesn't exist **")
                    break
                if obj[key].__class__.__name__ == list_of_str[0]:
                    print(obj[key])
            else:
                print(obj[key])

    def do_update(self, arg):
        """It's a function that updates an instance based on the class name and id."""

        list_of_str = arg.split()

        if len(list_of_str) == 0:
            print("** class name missing **")
        elif list_of_str[0] not in classes:
            print("** class doesn't exist **")
        elif len(list_of_str) == 1:
            print("** instance id missing **")

        else:
            obj_key = list_of_str[0] + "." + list_of_str[1]
            all_obj = storage.all()
            the_instance = 0

            for key, value in all_obj.items():
                if key == obj_key:
                    the_instance = value

            if not the_instance:
                print("** no instance found **")
            elif len(list_of_str) == 2:
                print("** attribute name missing **")
            elif len(list_of_str) == 3:
                print("** value missing **")
            else:
                setattr(the_instance, list_of_str[2], list_of_str[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
