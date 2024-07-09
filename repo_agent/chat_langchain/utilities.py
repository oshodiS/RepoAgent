
import os, json,re
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

def split_documents(doc, chunk_size=250, chunk_overlap=30):
        """ Split a document into chunks of text."""

        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on, strip_headers=False
        )
        md_header_splits = markdown_splitter.split_text( doc.page_content)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

        # Split
        splits = text_splitter.split_documents(md_header_splits)
    
        return splits


def get_chunk_with_source(docs, chunk_size=250, chunk_overlap=30):
        all_splits = []
        for doc in docs:
            splits = split_documents(doc, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            for doc_split in splits:
                filename = os.path.basename(list(doc.metadata.values())[0])
                doc_split.metadata = {'source':filename}        
            all_splits.extend(splits)
        return all_splits

def filter_docs(docs):
        return [doc for doc in docs if "summary.md" in doc.metadata['source']]

def get_json_from_path(path):
    with open(path, 'r', encoding='utf-8') as file:
           return json.load(file)
    
def get_qa_system_prompt():
    return (
            "You are an assistant for question-answering tasks regarding code documentation file. "
            "Use the following pieces of retrieved context to answer the question. It's also specified the name of the file that contains the functions. "
            "If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise."
            "\n\n"
            "{context}"
        )
def get_contextualize_q_system_prompt():
    return (
            "Given a chat history and the latest user question which might reference context in the chat history, "
            "formulate a standalone question which can be understood without the chat history. "
            "Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
            "Do NOT add requests for additional information or clarification if not in the original question."
            "keep it as a question"
        )
def get_dont_contextualize_system_prompt():
    return (
            "Repeat the question as it is. Do NOT add requests for additional information or clarification if not in the original question."
            "Do NOT answer the question,"
            
        )

def get_readme_path(root_path):
    """Reads the README.md file in the root of the repository."""
    readme_files = []
    pattern = re.compile(r'^(read[_]?me)([_]?(md|txt))$', re.IGNORECASE)
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if pattern.match(file):
                return os.path.join(root, file)
    return None

