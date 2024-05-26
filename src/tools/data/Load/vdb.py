from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

#TODO: Save real information
#=======================================================
#TODO: UNTESTEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#=======================================================

class Vdb():
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        # Access the API key
        self.api_key = os.getenv('PINECONE_API_KEY')
        self.pc = Pinecone(api_key=self.api_key)
        self.index_name = "parallaile-index"

    def first_setup(self):
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

    def write_resume_vector(self, values):
        namespace = "resume"

        #TODO: Make a smart id creator
        #latest_id = max(self.pc.Index(self.index_name).list(namespace=namespace))

        self.write_vector("0", values, namespace)

    def write_vector(self, id, values, namespace):
        index = self.pc.Index(self.index_name)

        index.upsert(
            vectors=[
                {"id": id, "values": values}
            ],
            namespace=namespace
            )
