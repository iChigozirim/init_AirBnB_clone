#!/usr/bin/python3
"""Defines the AirBnB console. """
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
