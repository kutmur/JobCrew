# tools/search_tools.py

import os
from dotenv import load_dotenv
from crewai.tools import tool
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()


@tool("Job Search Tool")
def job_search_tool(query: str) -> str:
    """
    A tool to search for job listings online.
    
    IMPORTANT: The 'query' parameter must be a single string, NOT a dictionary or JSON object.
    
    Args:
        query (str): A plain text search query string containing the position, location,
                     salary expectations, and other job preferences all in one line.
    
    Example of CORRECT usage:
        query = "Senior Python Developer remote full-time salary $100000-$130000"
    
    Example of INCORRECT usage (DO NOT DO THIS):
        query = {"description": "Senior Python Developer...", "type": "str"}  # WRONG!
    
    Simply pass all your search criteria as a single, natural language string.
    """
    serper_tool = SerperDevTool()
    # SerperDevTool.run() expects the search query directly without 'search_query=' parameter
    return serper_tool.run(search_query=f"Search for '{query}' job listings")


def serper_search_tool():
    """
    Returns a direct instance of SerperDevTool for general web searches.
    
    Returns:
        SerperDevTool: An instance of SerperDevTool for web searches
    """
    return SerperDevTool()