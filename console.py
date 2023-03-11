#!/usr/bin/python3
"""_summary"""

import cmd


class HBNBCommand(cmd.Cmd):

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
