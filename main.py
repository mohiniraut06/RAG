import os
import numpy
import logging
from pathlib import Path
from domain.document import PDFDocument,TXTDocument,Document
from infra.ingestion_source import LocalSource
from dotenv import load_dotenv

load_dotenv()

LOG_FILE = f"{os.getenv('FILE_LOG_PATH')}/app.log"
local_source_path = f"{os.getenv('LOCAL_SOURCE_PATH')}"

# LOG_DIR = Path(os.getenv("FILE_LOG_PATH"))

# LOG_DIR.mkdir(parents=True,exist_ok=True)

# LOG_FILE = LOG_DIR/"app.log"

logging.basicConfig(level = logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s-  %(message)s",
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(LOG_FILE,"a")],
                    )


logger=logging.getLogger(__name__)


# print(os.getCwd())

"""
We have to creat a pdf class object


"""
def main():

    logger.info("Application started")
    # my sharepoint  download completed 
    try:
        logger.info("Source files are being read here")

        #1)get filled from source

        local = LocalSource(local_source_path)
        localfiles = local.get_files()

        print(len(localfiles))

        logger.info(f"Total documents:- {Document.doc_counts}")
        logger.debug(f"PDF class Created")

        pdf1 = PDFDocument(
            docname="syallabus.txt",
            docsize=1024,
            createdat="2026-10-10",
            docpath=r""
        )

        logger.info(f"Total document:-{Document.doc_counts}")
        logger.debug(f"TXT class Created")

        txt1 = TXTDocument(
            docname="syallabus.txt",
            docsize=1024,
            createdat="2026-10-10",
            docpath=r""
        )

        pdf1.clean()

        # logger.info(f"Total document:-{Document.doc_counts}")

    except Exception:
         logger.exception("An unexpected error occurred ")
    finally:
        # pdf1.clean()
        
        logger.info("Application finished")



if __name__ == "__main__":
    main()
