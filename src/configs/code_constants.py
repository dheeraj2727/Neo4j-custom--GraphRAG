from pydantic import BaseModel
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv("./dev.env"))

class LLMConfig(BaseModel):
    openai_api_version: str = os.getenv("OPENAI_API_VERSION", "2023-03-15-preview")
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    openai_endpoint: str = os.getenv("OPENAI_ENDPOINT")
    openai_embedding_model: str = os.getenv("OPENAI_EMBEDDING_MODEL")
    openai_gpt_40_model: str = os.getenv("OPENAI_GPT_40_MODEL")
    openai_gpt_432k_model: str = os.getenv("OPENAI_GPT_432K_MODEL")

class GraphDBConfig(BaseModel):
    neo4j_uri: str = os.getenv("NEO4J_URI")
    neo4j_user: str = os.getenv("NEO4J_USER")
    neo4j_password: str = os.getenv("NEO4J_PASSWORD")

class VectorDBConfig(BaseModel):
    faiss_temp_path: str = "./src/db/temp_db/faiss_index"
    faiss_multi_doc_path:str = "./src/db/multi_documents/faiss_index"

class StorageConfig(BaseModel):
    dotnet_api :str = os.getenv("DOTNET_API")
    dir_path:str = "./data/"
    blob_api_url:str = f"http://{dotnet_api}/api/Documents?batchName="
    blob_download_path:str = ".src/data/downloaded_blobs/"

class DocuInsightsAPIConfig(BaseModel):
    dotnet_api :str = os.getenv("DOTNET_API")
    angular_url :str = os.getenv("ANGULAR_URL")
    docuInsights_prompts_api_url :str = f"http://{dotnet_api}/api/PromptList/"
    docuInsights_batch_report_api_url :str = f"http://{dotnet_api}/api/BatchExecutionReport/"


if __name__ == "__main__":
    llm_config = LLMConfig()
    graph_db_config = GraphDBConfig()
    vector_db_config = VectorDBConfig()
    storage_config = StorageConfig()
    docuinsights_api_config = DocuInsightsAPIConfig()
    
    print("LLM Config:", llm_config)
    print("Graph DB Config:", graph_db_config)
    print("Vector DB Config:", vector_db_config)
    print("Storage Config:", storage_config)
    print("DocuInsights API Config:", docuinsights_api_config)

  