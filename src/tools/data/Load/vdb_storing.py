from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

#TODO: Save real information

class vdb_storing():
    def __init__():
        # Load environment variables from .env file
        load_dotenv()
        # Access the API key
        api_key = os.getenv('PINECONE_API_KEY')

        pc = Pinecone(api_key=api_key)
        pc.create_index(
            name="quickstart",
            dimension=8, # Replace with your model dimensions
            metric="euclidean", # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ) 
        )