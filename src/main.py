import os

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

from tools.data.Extract.csv_extractor import CsvExtractor
from tools.data.Load.text_filewriter import TextFileWriter
from tools.data.Transform.preprocessing import preprocessing
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

def execute_pipeline(text):
    print("Before")
    print(text)
    print("----------------")
    preprocessed_text = preprocessing.preprocess_resume(text)
    print("After")
    print("----------------")
    print(preprocessed_text)


def get_first_row(path):
    # Example usage:
    loader = CsvExtractor(path)
    rows = loader.load_csv_data(num_rows=1, randomize=True)
    return rows[0][1]


if __name__ == '__main__':
    resume = get_first_row(DATASET_PATH)
    execute_pipeline(resume)
    #simple_gpt_prompt(resume)