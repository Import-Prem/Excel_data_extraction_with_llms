# Excel data extraction with Textbase

## Application Workflow: Generating SQL Queries and Filtering Data from Excel/CSV

**Step 1: Interaction with the Chatbot:**
1. Begin by interacting with the chatbot interface in plain text.
2. Ask your question or specify the data you're looking for within the conversation.

**Step 2: AI-Generated SQL Query:**
1. The chatbot leverages AI capabilities to generate an SQL query based on your input.
2. The AI crafts a query that corresponds to your request, ensuring syntactic correctness and alignment with the provided information.

**Step 3: Data Filtering from Excel/CSV:**
1. The chatbot processes the generated SQL query.
2. It applies the query to an Excel or CSV file containing relevant data.
3. The data filtering process extracts the specific information you're seeking from the dataset.

**Step 4: Presentation of Results in English:**
1. The chatbot takes the filtered data and presents it in an easily understandable English format.
2. The results are structured to provide clear insights into the extracted information.
3. You receive a concise, human-readable output that addresses your original query.

**Benefits and Features:**
- **User-Friendly Interaction:** The chatbot facilitates straightforward interactions through plain text conversations, eliminating the need for complex commands.
- **AI-Generated SQL Queries:** The AI's proficiency in query generation ensures accurate and relevant queries that reflect your intentions.
- **Dynamic Data Extraction:** The chatbot accesses Excel or CSV data and extracts information using the generated SQL query, allowing for dynamic data retrieval.
- **Readable Output:** The generated output is presented in an organized and understandable English format, providing meaningful insights.
- **Efficient Information Retrieval:** The application streamlines the process of querying and filtering data, making information retrieval more efficient.

**Usage Scenarios:**
- **Business Data Analysis:** Quickly retrieve and analyze specific business data from large datasets, enhancing decision-making processes.
- **Research and Reporting:** Efficiently gather research data and generate insightful reports without manual data sorting.
- **Educational Queries:** Facilitate learning by extracting relevant information from educational datasets for research or study purposes.

**Note:** Ensure the input provided to the chatbot is clear and accurate to obtain the desired results. Additionally, consider the security of sensitive data when utilizing any AI-based applications.


## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry shell
poetry install
```

## Start the development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.
> If you're using the default template, **remember to set the file path of the excel or csv** in `main.py`.
Run the following command:

```bash
poetry run python textbase/textbase_cli.py test main.py
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.



## Here is an example of the app

![testing](https://github.com/Import-Prem/Excel_data_extraction_with_llms/assets/84090854/6b1a32d4-13c5-434a-a131-2780747549a6)

