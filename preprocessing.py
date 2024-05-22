import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class preprocessing():
    def preprocess_resume(text):
        # Convert to lowercase
        text = text.lower()

        # Remove special characters and punctuation
        text = re.sub(r'[^\w\s]', ' ', text)

        # Normalize spaces
        text = re.sub(r'\s+', ' ', text).strip()

            # Tokenize text
        tokens = word_tokenize(text)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]

        # Join tokens back to string
        preprocessed_text = ' '.join(tokens)

        return preprocessed_text
