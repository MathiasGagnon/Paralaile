class Pipeline:

    def __init__(self, preprocessing, embedder):

        self.preprocessing = preprocessing
        self.embedder = embedder

    def execute_resume_analysis(self, resume):

        preprocessed_text = self.preprocessing.preprocess_resume(resume)

        embeddings = self.embedder.get_embeddings(preprocessed_text)
        
        return embeddings

    def analyse(self, data, embedding_model='text-embedding-ada-002', analysis='Resume'):

        embeddings = ""

        if analysis is 'Resume':
            embeddings = self.execute_resume_analysis(data)

        return embeddings

