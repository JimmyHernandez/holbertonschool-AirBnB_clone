#!/usr/bin/python3
""" Python Interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
If the user types 'x' or 'q', then quit the program.
param line: The entire string that the user has entered
return: True
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file command?"""
        if line == 'x' or line == 'q':
            return self.do_quit(line)

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
