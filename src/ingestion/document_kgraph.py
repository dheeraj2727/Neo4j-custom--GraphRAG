import os
from src.dataclass.document_file import DocumentFile, DocumentPage, Chunk, PageContent
from src.dataclass.knowledge_graph import KnowledgeGraph, Node, Relationship, Property

class DocumentKnowledgeGraph:
    def __init__(self,document_file: DocumentFile):
        self.document_file = document_file

    def create_document_node(self):
        contract_name,extention = os.path.splitext(self.document_file.name)
        node = Node(
            id=self.document_file.id,type="Document",
            properties=[Property(key="name",value=contract_name),
                        Property(key="file_path_url",value=self.document_file.file_path_url),
                        Property(key="doc_type",value=extention)])
        node.properties.append(Property(key="batch_id",value=self.document_file.batch_id))
        return node
    
    def create_page_nodes(self,page:DocumentPage):
        page_node = Node(
            id=page.id,
            type="Page",
            properties=[
                Property(key="page_number",value=page.page_number),
                Property(key="actual_char_count",value=page.actual_char_count),
                Property(key="img_data_url",value=page.img_data_url)
            ]
        )
        node.properties.append(key="batch_id",value=self.document_file.batch_id)
        return page_node