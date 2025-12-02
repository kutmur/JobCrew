"""
JobCrew Main Application
The main entry point for the Job Search application using CrewAI.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from jobcrew.agents import JobAgents
from jobcrew.tasks import JobTasks

class JobCrew:
    """
    Main JobCrew class to orchestrate the job search process.
    """
    
    def __init__(self, position, location, salary_expectations, employment_type):
        """Initialize JobCrew with user inputs."""
        self.position = position
        self.location = location
        self.salary_expectations = salary_expectations
        self.employment_type = employment_type
        
    def get_inputs(self):
        """
        Return inputs as a dictionary for CrewAI.
        """
        return {
            'position': self.position,
            'location': self.location,
            'salary_expectations': self.salary_expectations,
            'employment_type': self.employment_type
        }
    
    def run(self):
        """
        Execute the job search crew.
        """
        # Initialize agents and tasks
        agents = JobAgents()
        tasks = JobTasks()
        
        # Create agent instances
        researcher = agents.job_researcher()
        analyst = agents.job_analyst()
        strategist = agents.recruitment_strategist()
        
        # Create task instances
        research_task = tasks.job_research_task(researcher)
        analysis_task = tasks.job_analysis_task(analyst)
        report_task = tasks.reporting_task(strategist)
        
        # Set task dependencies manually after all tasks are created
        analysis_task.context = [research_task]
        report_task.context = [analysis_task]
        
        # Create the crew
        crew = Crew(
            agents=[researcher, analyst, strategist],
            tasks=[research_task, analysis_task, report_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew with proper inputs dictionary
        inputs_dict = self.get_inputs()
        print(f"\n🔍 Search Parameters: {inputs_dict}")
        
        result = crew.kickoff(inputs=inputs_dict)
        return result

def main():
    """
    Main function to run the JobCrew application.
    """
    # Load environment variables
    load_dotenv()
    
    # Validate required environment variables
    required_env_vars = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease check your .env file and ensure all required API keys are set.")
        return
    
    print("\n" + "=" * 70)
    print("🚀 Welcome to JobCrew - Your AI-Powered Job Search Assistant!")
    print("=" * 70)
    
    # Get user inputs
    try:
        position = input("\n💼 Enter the position you're looking for: ").strip()
        if not position:
            print("❌ Position cannot be empty.")
            return
            
        location = input("📍 Enter your preferred location (or 'Remote'): ").strip()
        if not location:
            print("❌ Location cannot be empty.")
            return
            
        salary = input("💰 Enter your salary expectations (e.g., '$80,000 - $100,000'): ").strip()
        if not salary:
            print("❌ Salary expectations cannot be empty.")
            return
            
        employment_type = input("⏰ Enter employment type (e.g., 'Full-time', 'Part-time', 'Contract'): ").strip()
        if not employment_type:
            print("❌ Employment type cannot be empty.")
            return
            
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using JobCrew! Good luck with your job search!")
        return
    
    print("\n" + "-" * 70)
    print(f"🔎 Searching for: {position}")
    print(f"📍 Location: {location}")
    print(f"💰 Salary: {salary}")
    print(f"⏰ Type: {employment_type}")
    print("-" * 70)
    print("\n🤖 Our AI agents are working on finding the best matches...")
    print("⏳ This may take a few minutes...\n")
    
    # Create and run JobCrew
    job_crew = JobCrew(position, location, salary, employment_type)
    
    try:
        result = job_crew.run()

        # Extract the final report
        final_report = result.raw if hasattr(result, 'raw') else str(result)

        # Display the final report
        print("\n" + "=" * 70)
        print("✅ YOUR JOB SEARCH REPORT IS READY!")
        print("=" * 70 + "\n")
        
        # Read and display the generated report file
        try:
            with open('jobs_report.md', 'r', encoding='utf-8') as f:
                report_content = f.read()
                print(report_content)
        except FileNotFoundError:
            # Fallback to raw result if file wasn't created
            print(final_report)
        
        print("\n" + "=" * 70)
        print("💾 Report saved as: jobs_report.md")
        print("🎯 Good luck with your applications!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ An error occurred during the job search: {str(e)}")
        print("🔧 Debug info: Check that all agents and tasks are properly configured.")
        print("💡 Please verify your API keys and internet connection, then try again.")

if __name__ == "__main__":
    main()
