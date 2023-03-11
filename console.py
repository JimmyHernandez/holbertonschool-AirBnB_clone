#!/usr/bin/python3
"""Write a program called console.py that contain the entry point of the\
    command interpreter."""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
