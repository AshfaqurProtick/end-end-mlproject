from setuptools import find_packages, setup
from typing import List


# The typing module in Python is used to provide type hints.
# In Python, the -> symbol is used to indicate the return type of a function.
# The 'List' type hint in this code is used to specify the expected return type of the 'get_requirements()' function.
# Specifically, the 'List[str]' type hint indicates that the function returns a list of strings.
# 'file_path:str' indicates that the file_path parameter is expected to be a string.

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# readlines() method includes the newline character \n at the end of each line

setup(

name='mlprojects',
version= '0.0.1',
author= 'Ashfaqur Protick',
author_email= 'ashfaqur.protick@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')

)

