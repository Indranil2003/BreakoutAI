# # Install required libraries
# # pip install streamlit pandas google-api-python-client openai serpapi python-dotenv

# # Import necessary modules
# import streamlit as st
# import pandas as pd
# import openai
# from googleapiclient.discovery import build
# # from serpapi import GoogleSearch  # Correct import
# from serpapi import GoogleSearchResults
# import os
# from dotenv import load_dotenv  # Import dotenv for loading .env file

# # Load .env file
# load_dotenv()

# # Set API keys from the .env file
# openai.api_key = os.getenv("OPENAI_API_KEY")
# SERP_API_KEY = os.getenv("SERP_API_KEY")

# # Define functions for data processing, search, and LLM interaction

# def process_csv_file(file):
#     """Process the uploaded CSV file."""
#     data = pd.read_csv(file)
#     return data

# def search_web(entity, query_template):
#     """Perform web search using SerpAPI."""
#     search_query = query_template.replace("{entity}", entity)
#     params = {
#         "q": search_query,
#         "api_key": SERP_API_KEY,
#     }
#     # search = GoogleSearch(params)  # Correct usage of GoogleSearch
#     search = GoogleSearchResults(params)  # Use GoogleSearchResults here
#     results = search.get("organic_results", [])
#     return results

# def extract_information(search_results, prompt_template):
#     """Extract information from web search results using LLM."""
#     prompt = prompt_template + "\n" + "\n".join(
#         [result['snippet'] for result in search_results if 'snippet' in result]
#     )
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=100
#     )
#     return response["choices"][0]["text"].strip()

# # Streamlit Dashboard Implementation

# st.title("AI Data Extraction Agent")

# # File upload
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
# if uploaded_file:
#     data = process_csv_file(uploaded_file)
#     st.write("## Uploaded Data Preview")
#     st.dataframe(data.head())
    
#     # Query input
#     query_template = st.text_input("Enter query template (use {entity} for placeholders)", "Get the email address of {entity}")
#     prompt_template = st.text_area("Enter LLM prompt template", "Extract the email address from the following results:")

#     # Process data
#     if st.button("Process Data"):
#         results = []
#         for entity in data.iloc[:, 0]:
#             search_results = search_web(entity, query_template)
#             extracted_info = extract_information(search_results, prompt_template)
#             results.append({"Entity": entity, "Extracted Info": extracted_info})
        
#         # Display results
#         results_df = pd.DataFrame(results)
#         st.write("## Extraction Results")
#         st.dataframe(results_df)
        
#         # Download results
#         csv = results_df.to_csv(index=False).encode('utf-8')
#         st.download_button("Download Results", csv, "results.csv", "text/csv")



# Install required libraries
# pip install streamlit pandas google-api-python-client openai serpapi python-dotenv

# Import necessary modules
import streamlit as st
import pandas as pd
import openai
import serpapi  # Corrected import
import os
from dotenv import load_dotenv  # Import dotenv for loading .env file

# Load .env file
load_dotenv()

# Set API keys from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

# Define functions for data processing, search, and LLM interaction

def process_csv_file(file):
    """Process the uploaded CSV file."""
    data = pd.read_csv(file)
    return data

def search_web(entity, query_template):
    """Perform web search using SerpAPI."""
    search_query = query_template.replace("{entity}", entity)
    params = {
        "q": search_query,
        "api_key": SERP_API_KEY,
    }
    # Using serpapi.search() instead of GoogleSearch
    search = serpapi.search(params)  # Correct usage
    results = search.get("organic_results", [])  # Get results from search
    return results

def extract_information(search_results, prompt_template):
    """Extract information from web search results using LLM."""
    prompt = prompt_template + "\n" + "\n".join(
        [result['snippet'] for result in search_results if 'snippet' in result]
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response["choices"][0]["text"].strip()

# Streamlit Dashboard Implementation

st.title("AI Data Extraction Agent")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = process_csv_file(uploaded_file)
    st.write("## Uploaded Data Preview")
    st.dataframe(data.head())
    
    # Query input
    query_template = st.text_input("Enter query template (use {entity} for placeholders)", "Get the email address of {entity}")
    prompt_template = st.text_area("Enter LLM prompt template", "Extract the email address from the following results:")

    # Process data
    if st.button("Process Data"):
        results = []
        for entity in data.iloc[:, 0]:
            search_results = search_web(entity, query_template)
            extracted_info = extract_information(search_results, prompt_template)
            results.append({"Entity": entity, "Extracted Info": extracted_info})
        
        # Display results
        results_df = pd.DataFrame(results)
        st.write("## Extraction Results")
        st.dataframe(results_df)
        
        # Download results
        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results", csv, "results.csv", "text/csv")
