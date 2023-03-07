from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .' # used in requirements.txt 

def get_requirements(file_path:str) -> List[str]:
    '''
    what kind of input parameter is given like path and it should read it 
    
    So, this function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # by default readlines from file_obj will add \n in list while reading it,to remove it we will use following
        requirements = [req.replace("\n", "") for req in requirements]
        # after this we will add -e . in requirements to automatically trigger setup.py file

        # Now while running this code -e . will also come in requirements to remove it we will use following
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



# Below setup is writing of metadat information about the entire project 
setup(
    name='mlproject', 
    version= '0.0.1', 
    author= 'Sushil', 
    author_email='sushildeore99@gmail.com', 
    packages = find_packages(), 
    install_requires = get_requirements('requirements.txt') # Previously it was ['pandas', 'numpy', 'seaborn'] but cannot define all here so creating function get_requiremets to have all
)