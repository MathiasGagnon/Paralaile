from openai import OpenAI
from dotenv import load_dotenv

import os

class Embedder:
    def __init__(self, model='text-embedding-ada-002'):
        self.model = model

        load_dotenv()

        self.client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),  # this is also the default, it can be omitted
        )
    
    def get_embeddings(self, text):
        """
        Embedds the input tokens with the specified model.

        Args:
        - tokens: Tokens to embedd.

        Returns:
        - The embeddings.
        """
        response = self.client.embeddings.create(
            input=[text],
            model=self.model
        )
        
        embeddings = response.data[0].embedding
        return embeddings
