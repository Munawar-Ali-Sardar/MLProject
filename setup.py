from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(path:str)->List[str]:
    with open(path) as file_obj:
        requirement = file_obj.readlines()
        requierments = [req.replace("\n", "") for req in requirement]

        if HYPEN_E_DOT in requierments:
            requierments.remove(HYPEN_E_DOT)
        
        return requierments

setup(
    name = "MLProject", 
    version="0.0.1",
    author= "munawar ali sardar", 
    author_email="me.munawar@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)