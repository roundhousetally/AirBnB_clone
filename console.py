#!/usr/bin/python3
""" Console """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ command interpreter for airbnb """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ exit the app """
        sys.exit(1)

    def help_quit(self):
        """ help for quit """
        print("Quit command to exit the program")

    do_EOF = do_quit

if __name__ == '__main__':
    """ cannot execute if imported """
    HBNBCommand().cmdloop()
