from src.configs.code_constants import StorageConfig
from src.logging.logger import logger
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from azure.storage.blob import BlobClient
import os
import requests

class DocumentHandler:
    def __init__(self):
        pass
    def read_pdfs(self,file_path):
        try:
            loader  = PyPDFLoader(file_path)
            document = loader.load()
            return document
        except Exception as e:
            logger.error(f"Error reading PDF file {file_path}: {e}")

    async def get_document_api(self,batch_name):
        try:
            storage_config = StorageConfig()
            blob_api_url = storage_config.blob_api_url + batch_name
            response = requests.get(blob_api_url)
            response.raise_for_status()
            document_api_info = response.json()
            return document_api_info
        except Exception as e:
            logger.error(f"Error fetching document API for batch {batch_name}: {e}")

    async def download_blob_to_memory(self,blob_url,target_folder,target_file_name):
        try:
            blob_cilent = BlobClient.from_blob_url(blob_url)
            await self.check_and_create_path(target_folder)
            file_path = os.path.join(target_folder,target_file_name)
            with open(file_path,"wb") as download_file:
                download_stream = blob_cilent.download_blob()
                download_file.write(download_stream.readall())
            return file_path
        except Exception as e:
            logger.error(f"Error downloading blob from {blob_url}: {e}")

    async def delete_downloaded_blobs(self,path):
        try:
            if os.path.exists(path):
                os.remove(path)
                logger.info(f"Deleted downloaded blob at {path}")
            else:
                logger.warning(f"File at {path} does not exist")
        except Exception as e:
            logger.error(f"Error deleting downloaded blob at {path}: {e}")

    async def check_and_create_path(self,path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                logger.info(f"Created directory at {path}")
        except Exception as e:
            logger.error(f"Error creating directory at {path}: {e}")

if __name__ == "__main__":
    batch_id = "sample_batch"
    document_handler = DocumentHandler()
        
               