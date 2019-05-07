"""

Install and use external modules

We can use the package manager PIP - Python Installer Package

See: https://pypi.org

pip3 install <package_name>

------------------------------------
------------------------------------
------------------------------------

# Example 1
from colorama import init, Fore, Back, Style
# Example 1
print('------------------------------------')
init()
print(Fore.RED + 'some red text')
print(Fore.MAGENTA + 'some magenta text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
"""

# Example 2
import pydf

print('------------------------------------')

# Example 2
pdf = pydf.generate_pdf('<h1>Rodrigo Cantarino on PYTHON!!!! </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
