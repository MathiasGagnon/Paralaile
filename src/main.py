import os

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

from tools.data.Extract.csv_extractor import CsvExtractor
from tools.data.Load.text_filewriter import TextFileWriter
from tools.data.Transform.preprocessing import Preprocessing
from tools.data.Transform.tokenization import Tokenizer
from tools.data.Transform.embedding import Embedder

from pipeline import Pipeline

from common.constants import *

def simple_gpt_prompt(resume):
    # Load environment variables from .env file
    load_dotenv()
    # Access the API key
    api_key = os.getenv('OPENAI_API_KEY')

    llm = OpenAI(temperature=0.9)

    template = """
    You are a recuiter for a highly efficient company. Your job is to look at resumes and help categorize them
    by following the o*net soft skills and technology skills. You will list these skills in a bullet point list only
    containing the skills without more detail and you will add 5 point list of the best jobs such a person could do.
    Here is the resume to analyse: {resume}
    """

    prompt = PromptTemplate(
        input_variables = ["resume"],
        template=template
    )

    text_to_save = prompt.format(resume=resume)

    #text_to_save = text_to_save + llm(prompt.format(resume=resume))

    print(text_to_save)

    text_writer = TextFileWriter(OUTPUTTXT_PATH, append=True, newline=True)
    text_writer(text_to_save)

def execute_v0_pipeline(text):
    print("Before")
    print(text)
    print("----------------")
    preprocessed_text = Preprocessing.preprocess_resume(text)
    print("After")
    print("----------------")
    print(preprocessed_text)


def get_first_row(path):
    # Example usage:
    loader = CsvExtractor(path)
    rows = loader.load_csv_data(num_rows=1, randomize=True)
    return rows[0][1]

def use_resume_pipeline():

    preprocessing = Preprocessing()
    embedder = Embedder('text-embedding-ada-002')

    pipeline = Pipeline(preprocessing, embedder)

    # Sample resume text
    resume_text = get_first_row(DATASET_PATH)

    # Process the resume text through the pipeline
    embeddings = pipeline.analyse(resume_text, analysis='Resume')

    # Print embeddings (for demonstration purposes)
    print("Embeddings:", embeddings)


if __name__ == '__main__':
    #resume = get_first_row(DATASET_PATH)
    #execute_v0_pipeline(resume)
    #simple_gpt_prompt(resume)
    use_resume_pipeline()