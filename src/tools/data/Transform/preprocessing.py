import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class Preprocessing:
    def preprocess_resume(text):
        """
        Preprocess resumes from the resume dataset before tokenization.

        Args:
        - text: Text to preprocess.

        Returns:
        - The preprocessed text.
        """

        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        tokens = word_tokenize(text)
        
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        
        preprocessed_text = ' '.join(tokens)
        
        # TODO: Handle special information like date/time, currency, etc. Evaluate the requirements for these formats
        
        return preprocessed_text
