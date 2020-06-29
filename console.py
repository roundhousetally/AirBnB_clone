#!/usr/bin/python3
""" Console """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ command interpreter for airbnb """
    prompt = '(hbnb) '
    __classes = { "BaseModel" }

    def do_quit(self, arg):
        """ exit the app """
        sys.exit(1)

    def help_quit(self):
        """ help for quit """
        print("Quit command to exit the program")

    do_EOF = do_quit

    def emptyline(self):
        """ does nothing with an empty line """
        pass

    def do_create(self, arg):
        """ creates a new instance of BaseModel """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        else:
            newstance = HBNBCommand.__classes[arg]()
            newstance.save()
            print(newstance.id)

    def do_show(self, arg):
        """ prints the string rep of an instance based upon class name """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif

    def do_destroy(self, arg):
        """ deletes and instance based upon class name """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif

    def do_all(self, arg):
if __name__ == '__main__':
    """ cannot execute if imported """
    HBNBCommand().cmdloop()
