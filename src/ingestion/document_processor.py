import asyncio,traceback
from datetime import datetime
from src.data import DocumentFile, DocumentPage, Chunk,PageContent
import fitz
import uuid
from src.models.embedding_models import azure_openai_embedding
import threading
lock = threading.Lock()
from src.models.reading_models import azure_openai_reason
from src.prompts.data_extraction_prompts import summary_extraction_prmopt
from src.logging.logger import logger
import concurrent.futures
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tenacity import retry, stop_after_attemt,wait_exponential

class DocumentProcessor:
    def __init__(self, document_file: DocumentFile):
        self.document_file = document_file
        self.llm=azure_openai_reason()

    async def generate_chunks_for_page(self,document_page: DocumentPage) -> list[Chunk]:
        embedding = azure_openai_embedding()
        @retry(stop=stop_after_attempt(), wait=wait_exponential(multiplier=1, min=4, max=10))
        def embed_chunk_with_retry(chunk_text):
            chunk = Chunk(id = uuid.uuid4(),text = chunk_text)
            chunk.char_count = len(chunk_text)
            chunk.embedding = embedding.embed_text(chunk_text)
            return chunk
        try:
            text_splitter = RecursiveCharacterTextSplitter(seperators=["\n\n", "\n", " ", ""], chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_text(document_page.content.text)
            if len(txt_chunk)>0 and len(txt_chunk[0])>50:
                