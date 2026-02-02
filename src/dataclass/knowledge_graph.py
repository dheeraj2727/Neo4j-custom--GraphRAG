from langchian.graph.graph_document import (Node as BaseNode,
                                            Relationship as BaseRelationship)
from typing import Optional, List,Any
from pydantic import BaseModel, Field

class Property(BaseModel):
    key: str
    value: Any

class Node(BaseNode):
    properties: Optional[List[Property]] = Field(None,description="List of properties for the node")

class Relationship(BaseRelationship):
    properties: Optional[List[Property]] = Field(None,description="List of properties for the relationship")

class KnowledgeGraph(BaseModel):
    nodes: List[Node] = Field([],description="List of nodes in the knowledge graph")
    relationships: List[Relationship] = Field([],description="List of relationships in the knowledge graph")