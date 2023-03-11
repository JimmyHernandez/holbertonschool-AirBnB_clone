#!/usr/bin/python3
"""Python Interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the command interpreter."""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End of file command."""
        return True

    def emptyline(self):
        """Empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
