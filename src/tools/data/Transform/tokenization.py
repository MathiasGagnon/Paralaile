import tiktoken

class Tokenizer:
    def __init__(self, model='gpt-3.5-turbo'):
        self.tokenizer = tiktoken.get_encoding(model)
    
    def tokenize(self, text):
        """
        Tokenizes the input text to the format needed by the selected llm before embedding .

        Args:
        - text: Text to tokenize.

        Returns:
        - The tokenized text.
        """
        tokens = self.tokenizer.encode(text)
        return tokens
