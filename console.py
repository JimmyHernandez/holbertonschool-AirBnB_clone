#!/usr/bin/python3
""" Python Interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """If the user types 'x' or 'q', then quit the program.
param line: The entire string that the user has entered
return: True
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """End of file command."""
        return True

    def emptyline(self):
        """Pass is a null operation; nothing happens when it executes."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
