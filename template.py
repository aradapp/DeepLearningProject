#This is to create folder structure
import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')
project_name = "cnnClassifies"
list_of_files = [
    #This is for CI CD pipeline. Main.yaml file will be saved here
    ".github/workflows/.gitkeep", #Why .gitkeep file, because empty folder will not be reflected in github
     f"src/{project_name}/__init__.py",
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/config/__init__.py",
     f"src/{project_name}/config/configuration.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",
     "params.yaml",
     "dvc.yaml",
     "requirement.txt",
     "setup.py",
     "research/trials.ipynb"
     
]

for file_path in list_of_files:
    #Handle forward slash path as window uses backward slash
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath) # this will separate the folder and file name

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) # if already created, don't create
        logging.info(f"Creating directory for the file {filedir} for file {filename}")

    #Checking is the file exist or not with the entire path or is the size of the file is 0 means empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass #Only create the file
        logging.info(f"Creating file {filepath}")

    else:
        #File already exist or not empty
        logging.info(f"File already exist {filepath}")


        