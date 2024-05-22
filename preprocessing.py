import re

class preprocessing():
    def preprocess_resume(text):
        # Convert to lowercase
        text = text.lower()

        # Remove special characters and punctuation
        text = re.sub(r'[^\w\s]', ' ', text)

        # Normalize spaces
        text = re.sub(r'\s+', ' ', text).strip()

        return text
