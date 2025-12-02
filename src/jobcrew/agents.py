"""
JobCrew Agents Definition
Implements all agents for job search and recruitment
"""

import os
from crewai import Agent
from jobcrew.tools.search_tools import job_search_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class JobAgents:
    """
    Contains all agent definitions for the JobCrew application.
    Each agent specializes in a specific aspect of job search and recruitment.
    """
    
    def __init__(self):
        pass
    
    def job_researcher(self):
        """
        Agent 1: Job Researcher Agent
        Specializes in finding relevant job opportunities online.
        """
        return Agent(
            role="Senior Talent Acquisition Specialist",
            goal="Find the most relevant and promising job opportunities online based on the user's specific criteria (position, location, salary, employment type).",
            backstory="An expert digital recruiter with a knack for navigating the web to unearth hidden job gems. You are a master of search queries and know exactly where to look for fresh, high-quality job postings.",
            tools=[job_search_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def job_analyst(self):
        """
        Agent 2: Job Analyst Agent
        Analyzes job postings to validate match with requirements.
        """
        return Agent(
            role="Job Requirements and Culture Analyst",
            goal="Analyze each job posting found by the researcher to extract critical details. Validate if the job truly matches the user's requirements for salary, location proximity, and work hours.",
            backstory="A meticulous and detail-oriented analyst. You have a sharp eye for reading between the lines of a job description, identifying key requirements, and assessing if a role is a genuine fit. You discard any listings that are not a perfect match.",
            tools=[job_search_tool],
            verbose=True,
            allow_delegation=False
        )
    
    def recruitment_strategist(self):
        """
        Agent 3: Recruitment Strategist Agent
        Synthesizes findings into actionable reports.
        """
        return Agent(
            role="Lead Recruitment Report Strategist",
            goal="Synthesize the filtered job listings into a clear, concise, and actionable report for the user. Select the absolute top 5 matches and present them in a structured format.",
            backstory="A seasoned recruitment manager and communicator who excels at turning raw data into strategic insights. Your reports are legendary for their clarity and empower job seekers to take immediate, effective action.",
            verbose=True,
            allow_delegation=False
        )
