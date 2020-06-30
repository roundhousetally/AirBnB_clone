#!/usr/bin/python3
""" Console """
import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter for airbnb """
    prompt = '(hbnb) '
    __classes = {"BaseModel"}

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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg[0], arg[1])
        not in FileStorage.__objects.keys():
            print("** no instance found **")
        else:
            keyval = "{}.{}".format(arg[0], arg[1])
            print(FileStorage.__objects[keyval])

    def do_destroy(self, arg):
        """ deletes and instance based upon class name """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objs.keys():
            print("** no instance found **")
        else:
            keyval = "{}.{}".format(arg[0], arg[1])
            FileStorage.pop(keyval)

    def do_all(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
#        else:
            #print them all

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in objs.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            keyval = "{}.{}".format(arg[0], arg[1])
            FileStorage.__objects[keyval] = args[4]


if __name__ == '__main__':
    """ cannot execute if imported """
    HBNBCommand().cmdloop()
