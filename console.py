#!/usr/bin/python3
""" Console """
import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter for airbnb """
    prompt = '(hbnb) '
    __classes = {"BaseModel": BaseModel,
                 "User": User,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Place": Place,
                 "Review": Review}

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
        elif arg not in HBNBCommand.__classes:
            print("** class does not exist **")
        else:
            newstance = HBNBCommand.__classes[arg]()
            newstance.save()
            print(newstance.id)

    def do_show(self, arg):
        """ prints the string rep of an instance based upon class name """
        args = arg.split()
        all_obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_obj.keys():
            print("** no instance found **")
        else:
            keyval = "{}.{}".format(args[0], args[1])
            print(all_obj[keyval])

    def do_destroy(self, arg):
        """ deletes and instance based upon class name """
        args = arg.split()
        all_obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_obj.keys():
            print("** no instance found **")
        else:
            keyval = "{}.{}".format(args[0], args[1])
            all_obj.pop(keyval)
            storage.save()

    def do_all(self, arg):
        args = arg.split()
        all_obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ret = []
            for i in all_obj.keys():
                ret.append(all_obj[i].__str__())
            print(ret)

    def do_update(self, arg):
        args = arg.split()
        all_obj = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_obj.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[3][0] == '"' and args[3][-1] == '"':
                v = args[3][1:-1]
            else:
                v = args[3]
            att = args[2]
            keyval = "{}.{}".format(args[0], args[1])
            all_obj[keyval].__dict__[att] = v
            storage.save()


if __name__ == '__main__':
    """ cannot execute if imported """
    HBNBCommand().cmdloop()
