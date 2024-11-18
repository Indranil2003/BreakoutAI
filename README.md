
# AI Data Extraction Agent

## Project Summary
The **AI Data Extraction Agent** is a Streamlit-based web application that enables users to upload a CSV file containing a list of entities (e.g., names, companies, etc.). The app will then use the SerpAPI to search the web for relevant information about each entity and extract the required details using OpenAI's GPT-3 model. The extracted information is displayed in a tabular format and can be downloaded as a CSV file.

The project leverages **SerpAPI** for web search functionality and **OpenAI's GPT-3 (text-davinci-003)** for processing and extracting information from the web search results.

## Features
- Upload a CSV file with a list of entities.
- Customize the search query template with placeholders.
- Extract relevant data (e.g., email addresses) from web search results.
- Display the extracted information in a table.
- Download the results as a CSV file.

## Setup Instructions

### Prerequisites
- Python 3.7 or later
- `pip` package manager

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Indranil2003/BreakoutAI.git
   cd BreakoutAI

   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file**:
   - Create a `.env` file in the project root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERP_API_KEY=your_serpapi_api_key
   ```

   - To get your keys:
     - [OpenAI API Key](https://platform.openai.com/signup)
     - [SerpAPI Key](https://serpapi.com/dashboard)

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

   - After running the command, you can access the application in your web browser at [http://localhost:8501](http://localhost:8501).

## Usage Guide

1. **Upload a CSV file**: 
   - The uploaded CSV should contain a list of entities (one per row). The app will use this data for performing web searches.
   
2. **Enter query template**: 
   - Input a query template with `{entity}` as a placeholder for the entities in your CSV file. For example: `"Get the email address of {entity}"`.

3. **Enter LLM prompt template**: 
   - Provide a prompt template that will guide the GPT-3 model on what information to extract from the search results. For example: `"Extract the email address from the following results:"`.

4. **Process Data**: 
   - Click the "Process Data" button to start the extraction process. The app will use the SerpAPI to search the web for each entity and then use OpenAI to extract the relevant information.

5. **View and Download Results**: 
   - After processing, the extracted data is shown in a table. You can download the results as a CSV file by clicking the "Download Results" button.

## Third-Party APIs and Tools Used

### 1. **SerpAPI**
   - **Website**: [https://serpapi.com](https://serpapi.com)
   - **Description**: SerpAPI is a service that provides search results from Google and other search engines. It is used in this project to perform web searches for each entity in the uploaded CSV file.
   - **API Key**: Required for usage. You can sign up and get an API key from [SerpAPI Dashboard](https://serpapi.com/dashboard).

### 2. **OpenAI (GPT-3)**
   - **Website**: [https://openai.com](https://openai.com)
   - **Description**: OpenAI provides GPT-3, a powerful language model that can be used for a variety of tasks, including extracting information from text. In this project, GPT-3 is used to process and extract relevant information from the search results obtained from SerpAPI.
   - **API Key**: Required for usage. You can sign up and get an API key from [OpenAI Platform](https://platform.openai.com/signup).

### 3. **Streamlit**
   - **Website**: [https://streamlit.io](https://streamlit.io)
   - **Description**: Streamlit is a Python library for creating custom web applications for data science and machine learning projects. It is used to create the interactive dashboard for this application.

### 4. **Pandas**
   - **Website**: [https://pandas.pydata.org](https://pandas.pydata.org)
   - **Description**: Pandas is a Python library used for data manipulation and analysis. In this project, it is used to process and manage the uploaded CSV file and the results of the extracted data.

## Troubleshooting
- **"API Key Error"**: Ensure that you have entered valid API keys in the `.env` file.
- **"CSV File Error"**: Make sure your CSV file has the correct format, with one entity per row in the first column.
- **"Streamlit Not Running"**: Ensure you have installed all the required dependencies and activated your virtual environment.


