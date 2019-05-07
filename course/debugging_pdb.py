"""

Debugging with PDB

PDB -> Python Debugger

From Python 3.7, we don't need to import PDB library. Now there is a builtin function called breakpoint().


"""
# Basic commands on PDB
# l -> list where we are on code
# n -> next line
# p -> print variable
# c -> continue the code execution

# import pdb

first_name = 'Rodrigo'
middle_name = 'Cantarino'
last_name = 'de Oliveira'
# pdb.set_trace()
breakpoint()

# On line import
# import pdb; pdb.set_trace()

full_name = first_name + ' ' + middle_name + ' ' + last_name



