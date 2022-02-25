#!/usr/bin/python3
"""Defines the AirBnB console. """
import cmd
import models
from models.base_model import BaseModel

CLASSES = [
    "BaseModel"
]


def parse_line(line):
    """Returns  of a list of all strings in a line"""
    if len(line) < 1:
        return ([])
    commands = line.split(" ")
    return (commands)

def validate_args(args, require_id="n", instance=''):
    """Returns True if a class and it's id exists and are
    not missing. Otherwise return False.
    
        Args:
            args (list): List of all arguments
            require_id (str): A string.
                              if it's == "y", the function would validate
                              instance id. Otherwise it wouldn't.
            instance (class): Class - to access class attributes.
    - If the class name is missing, print ** class name missing **
    - If the class name doesn’t exist, print ** class doesn't exist **
    - If the id is missing, print ** instance id missing **
    - If the instance of the class name doesn’t exist for the id,
        print ** no instance found **
    """
    try:
        class_name = args[0]

        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return (False)
    except IndexError:
        print("** class name missing **")
        return (False)

    if require_id == "y":
        try:
            id = args[1]

            key = "{}.{}".format(args[0], args[1])
            if key not in instance.storage.all():
                print("** no instance found **")
                return (False)
        except IndexError:
            print("** instance id missing **")
            return (False)
    return (True)

    



class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    storage = models.storage

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """On receiving end-of-file signal, exit the program."""
        return True

    def do_create(self, class_name):
        """ Creates a new instance of BaseModel, saves it and prints the id"""
        commands = parse_line(class_name)

        if validate_args(commands) == False:
            return

        self.new_obj = BaseModel()
        self.new_obj.save()
        print(self.new_obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        commands = parse_line(args)

        if validate_args(commands, "y", self) == False:
            return
        key = "{}.{}".format(commands[0], commands[1])
        print(self.storage.all()[key])
        
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        commands = parse_line(args)

        if validate_args(commands, "y", self) == False:
            return
        key = "{}.{}".format(commands[0], commands[1])
        del self.storage.all()[key]
        self.storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        or not on the class name.
        """
        commands = parse_line(arg)
        objects = self.storage.all().values()
        if len(commands) < 1:
            print([str(obj) for obj in objects])
        else:
            if commands[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                if commands[0] in str(obj)])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        commands = parse_line(args)

        if validate_args(commands, "y", self) == False:
            return
        if len(commands) < 3:
            print("** attribute name missing **")
            return
        if len (commands) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        obj = self.storage.all()[key]
        try:
            obj.commands[2] = commands[3]
        except AttributeError:
            setattr(obj, commands[2], commands[3])
        self.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
