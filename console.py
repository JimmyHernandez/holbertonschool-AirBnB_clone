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
        """Create a new instance of BaseModel."""
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
        """Destroys the current room and all the items in it."""
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

    def do_all(self, line):
        """Print all instances of a class."""
        arg = line.split()
        obj_dict = storage.all()
        res = []
        if not arg:
            for key, obj in obj_dict.items():
                res.append(str(obj))
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, obj in obj_dict.items():
                if obj.__class__.__name__ == arg[0]:
                    res.append(str(obj))

        print(res)

    def do_update(self, line):
        """Upates an instance by adding/updating a key-value pair."""
        args = line.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in obj_dict.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            setattr(obj, args[2], args[3])
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
