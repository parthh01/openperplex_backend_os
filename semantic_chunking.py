import os

# from semantic_router.encoders import CohereEncoder
# from semantic_chunkers import StatisticalChunker
from langchain_experimental.text_splitter import SemanticChunker
# from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# encoder = CohereEncoder(cohere_api_key=COHERE_API_KEY, input_type='search_document',
#                         name='embed-multilingual-v3.0')

# chunker = StatisticalChunker(encoder=encoder, max_split_tokens=200)





# text_splitter = SemanticChunker(OpenAIEmbeddings())
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
text_splitter = SemanticChunker(hf_embeddings)



def get_chunking(text):
    """
    Splits the provided text into meaningful chunks using a predefined chunker.

    Args:
    text (str): The text to be chunked.

    Returns:
    list: A list of chunks if the text is sufficiently long and non-empty; otherwise, an empty list.
    """
    try:
        # chunks = chunker(docs=[text])
        # values = [c.content for chunk in chunks for c in chunk]
        # return values
        docs = text_splitter.create_documents([text])
        return [doc.page_content for doc in docs]

    except Exception as e:
        print(f"Error during chunking process: {e}")
        return []
