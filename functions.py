import json
from llama_index.llms.anthropic import Anthropic
import pandas as pd
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import PromptTemplate


path = "D:/python projects/excel formula generator/alphabets.json"
with open(path, "r") as f:
    alphabets = json.load(f)


def get_coldata(csv_file):
    "Gets csv file as parameter and returns list of columns and 5 rows with column names and alphabets according to their column."
    alpha_colname=[]
    for col_name, char in zip(csv_file.columns, alphabets):
        col_data = col_name+" "+ str(csv_file[col_name].iloc[:5].tolist())
        alpha_colname.append(str((char,col_data)))
    
    return alpha_colname

def pipeline(api_key):

    llm = Anthropic(api_key=api_key, model="claude-3-haiku-20240307")

    prompt_str = """
                You are an Excel Formula Generation Assistant. Your task is to provide the appropriate Excel formula based on the user's request and the data provided in an Excel file.
                The user will provide a description of the operation they want to perform, and you need to generate the corresponding Excel formula that can be used on the given Excel data.

                For example, if the user requests:

                "Calculate the average of the 'Sales' column grouped by 'Region'"
                And the Excel file has columns like 'Region', 'Product', 'Sales', etc., then you should generate a formula like:

                =AVERAGEIFS(Sales, Region, Region)

                Here are a few more examples of possible user requests and the corresponding formulas:

                User: "Sum the 'Quantity' values where 'Category' is 'Furniture'"
                Formula: =SUMIFS(Quantity, Category, "Furniture")

                User: "Count the unique values in the 'City' column"
                Formula: =COUNTUNIQUE(City)

                User: "Concatenate 'First Name' and 'Last Name' columns with a space in between"
                Formula: =CONCATENATE(FirstName, " ", LastName)

                Your formulas should be accurate, handle potential errors or edge cases gracefully, and provide clear explanations if needed. You can also ask for clarification from the user if their request is ambiguous or if you need more information to generate the formula.
                To generate the formulas, you should understand the structure and content of the Excel data, including data types, column names, and relationships between different columns. You should also have a deep knowledge of Excel functions and their appropriate usage.
                Additionally, you may need to handle complex scenarios, such as data aggregation, conditional logic, array formulas, and nested functions. Your goal is to provide the user with the most efficient and accurate Excel formula to solve their problem.

    data = {data}
    \n
    {request}
    """
    prompt_template = PromptTemplate(prompt_str)
    pipeline = QueryPipeline(chain=[prompt_template, llm])

    return pipeline

