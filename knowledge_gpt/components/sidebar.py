import streamlit as st

#import faq
from dotenv import load_dotenv
import os

load_dotenv()





def faq():
    st.markdown(
        """
# FAQ
## How does KnowledgeGPT work?
When you upload a document, it will be divided into smaller chunks 
and stored in a special type of database called a vector index 
that allows for semantic search and retrieval.

When you ask a question, KnowledgeGPT will search through the
document chunks and find the most relevant ones using the vector index.
Then, it will use GPT3 to generate a final answer.

## Is my data safe?
Yes, your data is safe. KnowledgeGPT does not store your documents or
questions. All uploaded data is deleted after you close the browser tab.

## Why does it take so long to index my document?
If you are using a free OpenAI API key, it will take a while to index
your document. This is because the free API key has strict [rate limits](https://platform.openai.com/docs/guides/rate-limits/overview).
To speed up the indexing process, you can use a paid API key.

## What do the numbers mean under each source?
For a PDF document, you will see a citation number like this: 3-12. 
The first number is the page number and the second number is 
the chunk number on that page. For DOCS and TXT documents, 
the first number is set to 1 and the second number is the chunk number.

## Are the answers 100% accurate?
No, the answers are not 100% accurate. KnowledgeGPT uses GPT-3 to generate
answers. GPT-3 is a powerful language model, but it sometimes makes mistakes 
and is prone to hallucinations. Also, KnowledgeGPT uses semantic search
to find the most relevant chunks and does not see the entire document,
which means that it may not be able to find all the relevant information and
may not be able to answer all questions (especially summary-type questions
or questions that require a lot of context from the document).

But for most use cases, KnowledgeGPT is very accurate and can answer
most questions. Always check with the sources to make sure that the answers
are correct.
"""
    )





def sidebar():
    with st.sidebar:
        st.markdown(
            " "
            # "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            # "2. Upload a pdf, docx, or txt file📄\n"
            # "3. Ask a question about the document💬\n"
        )

        # api_key_input = st.text_input(
        #     "OpenAI API Key",
        #     type="password",
        #     placeholder="Paste your OpenAI API key here (sk-...)",
        #     help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
        #     value=os.environ.get("OPENAI_API_KEY", None)
        #     or st.session_state.get("OPENAI_API_KEY", ""),
        # )

        # api_key = st.session_state.get("OPENAI_API_KEY")

        # st.session_state["OPENAI_API_KEY"] = api_key
        
        
#        st.markdown("---")
        # st.markdown(
        #     "Continuamos mejorando."
        # )
        #st.markdown("Made by   [Jhon Glidden](https://twitter.com/mm_sasmitha)")
        # st.markdown("---")

        #faq()
