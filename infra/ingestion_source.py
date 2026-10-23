from abc import ABC, abstractmethod
from pathlib import Path
import os
import logging
logger = logging.getLogger(__name__)
"""

document source classess to downloaded file from.
it could be sharepoint,localFiles,googleDrive files etc

"""


class Injection_Source:

    """
    Base class for  ingestion source
    
    """
    @abstractmethod
    def get_files(self):
        pass


class SPsource(Injection_Source):
    pass


class LocalSource(Injection_Source):


    def __init__(self,path:str):
        self.path = path

    def get_files(self):
        """
        get the files from the path and store then in a list
        
        """
        logger.info("local files are being read")
        folder_path = Path(self.path)
        files = []

        for file in folder_path.iterdir():
            if file.is_file():
                files.append(file)

        return files


    
  


