#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Usage:
    dojo add_room <room_name> <room_type>
    dojo create_person <name> <person_type>[--Y | --N]
    dojo (-i | --interactive)
    dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
import Dojo_main


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:

            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print ('Invalid Command!')
            print (e)
            return
        except SystemExit:

            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyDojoInteracter(cmd.Cmd):

    intro = 'Welcome to Andela(Nairobi) Dojo!' \
        + ' (type help for a list of commands.)'
    prompt = '(**DOJO**) '
    dojo = Dojo_main.Dojo()
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: add_room <room_name> <room_type>"""

        MyDojoInteracter.dojo.create_room(arg['<room_name>'],
                arg['<room_type>'])

        # print(arg)

    @docopt_cmd
    def do_create_person(self, arg):
        """Usage: create_person <name> <person_type>[--Y | --N]"""

        MyDojoInteracter.dojo.add_person(arg['<name>'],
                arg['<person_type>'], 'Y')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print ('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyDojoInteracter().cmdloop()

print (opt)

			
