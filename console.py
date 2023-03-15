#!/usr/bin/python3
"""Write a program called console.py that contain the entry point of the\
    command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel": BaseModel}


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
        """Print the string "EOF" and then exits the program\
           :param line: The line of text that the user entered."""
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
        """Print the value of the variable named by the argument
        :param line: The line of text that the user entered."""

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
        """It destroys the current
        room and all the items in it
        :param line: The line of text that the user entered.
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
        pass

    def do_update(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
