
import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load environment variables from the .env file
load_dotenv()

# Set API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")

# Function to process the uploaded CSV file
def process_csv_file(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
        return None

# Function to perform a web search using SerpAPI
def search_web(entity, query_template):
    try:
        # Ensure that the entity is properly formatted for a search query
        search_query = query_template.replace("{entity}", entity.strip())  # Strip spaces if any
        params = {
            "q": search_query,
            "api_key": SERP_API_KEY,
        }
        search = GoogleSearch(params)
        results = search.get_dict().get("organic_results", [])
        return results
    except Exception as e:
        st.error(f"Error during web search: {e}")
        return []

# Function to extract information from search results using OpenAI LLM
def extract_information(search_results, prompt_template):
    try:
        if not search_results:
            return "No results found."
        
        # Combine search result snippets into a prompt
        search_content = "\n".join(
            [result.get('snippet', '') for result in search_results]
        )
        prompt = f"{prompt_template}\n{search_content}"

        # Use the ChatCompletion API for OpenAI >=1.0.0
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure you use a supported model
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )

        # Return the assistant's response
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        st.error(f"Error during information extraction: {e}")
        return "Extraction failed."

# Streamlit dashboard implementation
st.title("AI Data Extraction Agent")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = process_csv_file(uploaded_file)
    if data is not None:
        st.write("## Uploaded Data Preview")
        st.dataframe(data.head())
        
        # Query input
        query_template = st.text_input("Enter query template (use {entity} as a placeholder)", 
                                       "Get the email address of {entity}")
        prompt_template = st.text_area("Enter LLM prompt template", 
                                       "Extract the email address from the following results:")
        
        # Process data
        if st.button("Process Data"):
            results = []
            for entity in data.iloc[:, 0]:
                # Ensure the entity is in the right format for search
                search_results = search_web(str(entity), query_template)
                if search_results:
                    st.write(f"Search Results for {entity}: {search_results}")  # Display raw results for debugging
                extracted_info = extract_information(search_results, prompt_template)
                results.append({"Entity": entity, "Extracted Info": extracted_info})
            
            # Display results
            results_df = pd.DataFrame(results)
            st.write("## Extraction Results")
            st.dataframe(results_df)
            
            # Download results
            csv = results_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results", csv, "results.csv", "text/csv")
