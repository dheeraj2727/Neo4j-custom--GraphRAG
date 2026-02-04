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
        node = Node(
            id=page.id,
            type="Page",
            properties=[
                Property(key="page_number",value=page.page_number),
                Property(key="actual_char_count",value=page.actual_char_count),
                Property(key="img_data_url",value=page.img_data_url)
            ]
        )
        node.properties.append(key="batch_id",value=self.document_file.batch_id)
        return node
    
    def create_page_node(self,page: DocumentPage):
        node = Node(
            id=page.id,
            type="Page",
            properties=[
                Property(key="page_number",value=page.page_number),
                Property(key="actual_char_count",value=page.actual_char_count),
                Property(key="img_data_url",value=page.img_data_url)
            ]
        )
        node.properties.append(Property(key="batch_id",value=self.document_file.batch_id))
        return node
    
    def create_chunk_node(self,chunk: Chunk,source_doc:str):
        node = Node(
            id=chunk.id,
            type="Chunk",
            properties=[
                Property(key="chunk_text",value=chunk.text),
                Property(key="embed",value=chunk.embedding),
                Property(key="source_doc",value=source_doc)
            ]
        )
        node.properties.append(Property(key="batch_id",value=self.document_file.batch_id))
        return node
    
    def generate_document_graph(self,document_file: DocumentFile):
        nodes = list()
        rels = list()
        page_nodes = list()
        chunk_nodes = list()
        document_node = self.create_document_node()
        nodes.append(document_node)
        for i in range(len(document_file.pages)):
            page = document_file.pages[i]
            page_node = self.create_page_node(page)
            nodes.append(page_node)
            page_nodes.append(page_node)
            rels.append(
                Relationship(
                    start_node_id=document_node.id,
                    end_node_id=page_node.id,
                    type="HAS_PAGE",
                    properties=[]
                )
            )
            for j in range(len(page.chunks)):
                chunk = page.chunks[j]
                chunk_node = self.create_chunk_node(chunk,source_doc=document_file.name)
                nodes.append(chunk_node)
                chunk_nodes.append(chunk_node)
                rels.append(
                    Relationship(
                        start_node_id=page_node.id,
                        end_node_id=chunk_node.id,
                        type="HAS_CHUNK",
                        properties=[]
                    )
                )