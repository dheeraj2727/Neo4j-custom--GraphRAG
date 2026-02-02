from typing import List, Optional,Any
from pydantic import BaseModel, Field

class PageContent(BaseModel):
    text: str =Field(None, description="Text content of the page")
    summary: str =Field(None, description="Summary of the page content")
    sections: List[str] =Field(None, description="List of sections in the page")

class Chunk(BaseModel):
    id:Any
    text : str
    embedding: any: None
    char_count: int

class DocumentPage(BaseModel):
    id: Any
    source_doc: str
    page_number : int = None
    actual_char_count: int = None
    img_data_url :str = Field(default_factory=str)
    page_content: PageContent = None
    page_embedding :any= None
    chunks:List[Chunk]= Field(default_factory=list)

class DocumentFile(BaseModel):
    batch_id :int
    id= Any
    name:str
    file_path_url :str
    pages:List[DocumentPage]= Field(default_factory=list)
    total_num_of_pages:int = None
