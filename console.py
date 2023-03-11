#!/usr/bin/env python3
"""This module implements the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter."""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
