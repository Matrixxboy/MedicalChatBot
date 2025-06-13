import os
from pathlib import Path
import logging


# Configure logging before creating the Flask app
logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : [%(message)s]')  # Or DEBUG, WARNING, ERROR, CRITICAL

list_of_file = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trial.ipynb"
]

for filePath in list_of_file:
    filePath = Path(filePath)
    fileDir ,filename = os.path.split(filePath)
    
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating Directory ; {fileDir} for the file  : {filename}")
        
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as f:
            pass
        logging.info(f"Creating empty file  {filename}: {filePath}")
        
    else :
        logging.info(f"{filename} is already exist")