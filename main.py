import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List
import pandas as pd
from sqlite3 import connect

conn = connect(':memory:')

def get_excel_columns(excel_data):
    try:
        columns = excel_data.columns.tolist()
        return columns
    except Exception as e:
        print("Error:", e)
        return []   

def extract_data_from_excel(excel_data,sql_query):
    # Remove line breaks from sql_query
    sql_query = sql_query.replace('\n', ' ').replace("SQL Query: ","")
    # Execute the SQL query on the DataFrame
    result = pd.read_sql(sql_query,conn)
    if not result.empty:
        # Convert each row of the DataFrame to a formatted string
        result_rows = [", ".join(map(str, row)) for _, row in result.iterrows()]
        result_string = "\n".join(result_rows)
        return f"Extracted Data:\n{result_string}"

    else:
        return "No data found."


# Load your OpenAI API key
models.OpenAI.api_key = "PASTE_OPENAI_KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

file_path = r"elementary_2015_16.csv"  # Change the file path

if file_path.lower().endswith(".xlsx") or file_path.lower().endswith(".xls"):
    data = pd.read_excel(file_path, engine='openpyxl')
elif file_path.lower().endswith(".csv"):
    data = pd.read_csv(file_path)
else:
    print("Unsupported file format")
data.to_sql('test_data', conn)
columns_list = get_excel_columns(data)
print(columns_list)

if columns_list:
    print("Columns in Excel:")
    for column in columns_list:
        print(column)
else:
    print("No columns found.")

# Prompt for GPT-3.5 Turbo
@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information
    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    SYSTEM_PROMPT =  (
        "Generate a valid SQL query to extract information from the Excel sheet 'test_data'. "
        "Ensure that your query is syntactically correct and relevant to the following user input and columns:\n"
        f"User Input: {message_history[-1]} \n"
        f"Columns: {columns_list}\n"
        "SQL Query:"
    )

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1   

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,    
        message_history=message_history,
        model="gpt-3.5-turbo",
        max_tokens=100,
    )
    print("bot_response",bot_response)
    result = extract_data_from_excel(data,bot_response)
    print(result)           
    return result , state 

# # Close the connection
# conn.close()
# print("Connection closed")            
