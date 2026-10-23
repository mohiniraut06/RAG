
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class Document(ABC):
    """
    Base Document class which will be used by child subclasses.
    """

    doc_counts = 0

    def __init__(self,docname:str,docsize:int,docpath:str,createdat:str):
         self.docname = docname
         self.docsize = docsize
         self.docpath = docpath
         self.createdat = createdat

         Document.doc_counts+=1
        

    # def __init__(self, docname, docsize, docpath, createdat):
    #     self.docname = docname
    #     self.docsize = docsize
    #     self.docpath = docpath
    #     self.createdat = createdat

    @abstractmethod
    def extract(self):
        """
        abstract method for extracting the content

        """

        pass
    
    @abstractmethod
    def clean(self):
        """
        abstract method for cleaning the content of file

        """

        pass

class PDFDocument(Document):
    """
     Craeting a pdfdocument class from base class to perform pdf related activities

    """
    def __init__(self,docname:str,docsize:int,docpath:str,createdat:str):
        super().__init__(docname,docsize,docpath,createdat)
        self.filetype="PDF"

        # self.docname = docname
        # self.docsize = docsize
        # self.docpath = docpath
        # self.createdat = createdat

    def extract(self):
        print(f"{self.docname}content has bean extracted")
        return "The hr policy is going to expire"

    def clean(self):
        print(f"{self.docname}content has bean cleaned")
        
    
    

class TXTDocument(Document):
    """
     Craeting a pdfdocument class from base class to perform txt related activities

    """
    def __init__(self,docname:str,docsize:int,docpath:str,createdat:str ):
           super().__init__(docname,docsize,docpath,createdat)
           self.filetype="TXT"

    def extract(self):
        print(f"{self.docname}content has bean extracted")
        
    
    def clean(self):
        print(f"{self.docname}content has bean cleaned")


    
