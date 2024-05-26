from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

#TODO: Save real information
#=======================================================
#TODO: UNTESTEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#=======================================================

class vdb_storing():
    def __init__():
        # Load environment variables from .env file
        load_dotenv()
        # Access the API key
        self.api_key = os.getenv('PINECONE_API_KEY')
        self.pc = Pinecone(api_key=self.api_key)
        self.index_name = "parallaile-index"

    def first_setup():
        pc = self.pc
        index_name = self.index_name
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud='aws', 
                    region='us-east-1'
                ) 
            )

    def write_vector(id, values, namespace):
        index = pc.Index(self.index_name)

        index.upsert(
            vectors=[
                {"id": id, "values": values}
            ],
            namespace=namespace
            )
