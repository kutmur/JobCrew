"""
JobCrew Tasks Definition
Contains all task definitions for job search and recruitment workflow.
"""

from crewai import Task

class JobTasks:
    """
    Contains all task definitions for the JobCrew application.
    Each task corresponds to an agent's specific goal and responsibilities.
    """
    
    def job_research_task(self, agent):
        """
        Task for Job Researcher to find relevant job opportunities.
        """
        return Task(
            description="""
            Using the provided criteria:
            - Position: {position}
            - Location: {location}
            - Salary Expectations: {salary_expectations}
            - Employment Type: {employment_type}
            
            Conduct a thorough search for relevant job openings that match these criteria.
            
            Your task is to:
            1. Search for job postings that match the position title or related roles
            2. Filter for the specified location or remote opportunities if applicable
            3. Look for positions that meet or exceed the salary expectations
            4. Focus on the specified employment type (full-time, part-time, contract, etc.)
            5. Compile a comprehensive list of potential job postings
            
            For each job posting found, collect:
            - Job title
            - Company name
            - Location
            - URL to the job description
            - Brief summary of the role
            
            Cast a wide net to ensure we capture all relevant opportunities.
            """,
            agent=agent,
            expected_output="A list of job postings, each containing the job title, company name, location, and a URL to the job description."
        )
    
    def job_analysis_task(self, agent):
        """
        Task for Job Analyst to filter and analyze job postings.
        """
        return Task(
            description="""
            From the list of jobs provided by the researcher, analyze each job description in detail.
            
            Your task is to:
            1. Review each job posting thoroughly
            2. Filter out any jobs that do NOT explicitly meet the criteria:
               - Salary expectations: {salary_expectations}
               - Location requirements: {location}
               - Employment type: {employment_type}
            3. For jobs that DO match all criteria, extract:
               - Key responsibilities and duties
               - Required skills and qualifications
               - Preferred qualifications
               - Company culture indicators
               - Benefits and perks mentioned
            4. Assess the overall fit and quality of each remaining opportunity
            5. Rank the opportunities based on how well they match the user's profile
            
            Be strict in your filtering - only include jobs that truly meet ALL the specified requirements.
            Provide detailed analysis for each qualified job opportunity.
            """,
            agent=agent,
            expected_output="A filtered list of fully-vetted job opportunities with summarized details including required skills, key responsibilities, and why each job is a good match.",
            context=[]  # Will be set dynamically in main.py
        )
    
    def reporting_task(self, agent):
        """
        Task for Recruitment Strategist to create the final report.
        """
        return Task(
            description="""
            Review the final, filtered list of jobs from the analyst.
            
            Your task is to:
            1. Select the top 5 most promising opportunities from the filtered list
            2. For each of the top 5 jobs, compile:
               - Job Title
               - Company Name
               - Location
               - Why it's a great match (2-3 compelling sentences)
               - Key highlights (salary range if mentioned, notable benefits, growth opportunities)
               - Application URL
            3. Structure the information in a clean, professional Markdown format
            4. Add a brief executive summary at the top
            5. Include actionable next steps for the job seeker
            
            The report should be:
            - Professional and polished
            - Easy to scan and read
            - Action-oriented
            - Motivating and encouraging
            
            Format the report with clear headings, bullet points, and proper Markdown structure.
            Save the final report as 'jobs_report.md'.
            """,
            agent=agent,
            expected_output="A final Markdown file named jobs_report.md containing the top 5 job matches in a structured and readable format with executive summary and actionable recommendations.",
            context=[],  # Will be set dynamically in main.py
            output_file='jobs_report.md'
        )
