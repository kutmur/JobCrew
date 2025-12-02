# JobCrew Agents Documentation

## Overview

JobCrew employs a multi-agent architecture powered by CrewAI to provide intelligent job search capabilities. Each agent has a specific role, goal, and set of tools to accomplish their part of the job search workflow.

## Agent Architecture

### 1. Job Researcher Agent 🔍

**Role:** Senior Talent Acquisition Specialist

**Goal:** Find the most relevant and promising job opportunities online based on the user's specific criteria (position, location, salary, employment type).

**Backstory:** An expert digital recruiter with a knack for navigating the web to unearth hidden job gems. This agent is a master of search queries and knows exactly where to look for fresh, high-quality job postings.

**Tools:**
- Job Search Tool (powered by Serper API)
- Web search capabilities
- Real-time job listing discovery

**Responsibilities:**
- Execute targeted searches across job platforms
- Filter initial results by position, location, and employment type
- Compile comprehensive lists of potential opportunities
- Extract key information (title, company, location, URL)

**Output:** A curated list of job postings with basic information for further analysis.

---

### 2. Job Analyst Agent 📊

**Role:** Job Requirements and Culture Analyst

**Goal:** Analyze each job posting found by the researcher to extract critical details and validate if the job truly matches the user's requirements for salary, location proximity, and work hours.

**Backstory:** A meticulous and detail-oriented analyst with a sharp eye for reading between the lines of a job description. This agent identifies key requirements and assesses if a role is a genuine fit, discarding any listings that are not a perfect match.

**Tools:**
- Job Search Tool for detailed investigation
- Text analysis capabilities
- Pattern matching for requirements

**Responsibilities:**
- Review each job posting in detail
- Extract required and preferred qualifications
- Identify salary ranges and benefits
- Assess company culture indicators
- Filter out non-matching opportunities
- Rank opportunities by match quality

**Quality Criteria:**
- Salary expectations must match or exceed user requirements
- Location must be compatible with user preferences
- Employment type must match exactly
- Must have clear job responsibilities

**Output:** A filtered list of fully-vetted job opportunities with detailed analysis of skills, responsibilities, and fit assessment.

---

### 3. Recruitment Strategist Agent 📋

**Role:** Lead Recruitment Report Strategist

**Goal:** Synthesize the filtered job listings into a clear, concise, and actionable report for the user. Select the absolute top 5 matches and present them in a structured format.

**Backstory:** A seasoned recruitment manager and communicator who excels at turning raw data into strategic insights. Their reports are legendary for clarity and empower job seekers to take immediate, effective action.

**Tools:**
- No external tools needed (works with data from previous agents)
- Report generation capabilities
- Markdown formatting

**Responsibilities:**
- Review all filtered opportunities from the analyst
- Select the top 5 most promising matches
- Create compelling match rationales
- Structure information for easy scanning
- Provide actionable next steps
- Format reports professionally

**Report Structure:**
1. Executive Summary
2. Top 5 Job Matches (detailed)
   - Job Title & Company
   - Location
   - Match Rationale (why it's great)
   - Key Highlights
   - Application URL
3. Next Steps and Recommendations

**Output:** A polished Markdown report saved as `jobs_report.md` with top opportunities highlighted.

---

## Agent Workflow

The agents work in a **sequential process**, with each agent building on the work of the previous one:

```
User Input
    ↓
Job Researcher → Finds opportunities
    ↓
Job Analyst → Filters and analyzes
    ↓
Recruitment Strategist → Creates report
    ↓
Final Report (jobs_report.md)
```

## Agent Communication

Agents communicate through CrewAI's context system:
- **Analysis Task** receives context from Research Task
- **Reporting Task** receives context from Analysis Task
- Context includes all data, findings, and intermediate results

## Agent Configuration

All agents are configured with:
- `verbose=True` - Provides detailed output during execution
- `allow_delegation=False` - Each agent completes their own task independently

## Customization

You can customize agent behavior by modifying `src/jobcrew/agents.py`:

```python
# Example: Adjust agent verbosity
agent = Agent(
    role="...",
    goal="...",
    backstory="...",
    verbose=False,  # Change to False for less output
    allow_delegation=True  # Enable if you want agents to delegate tasks
)
```

## Best Practices

1. **Be Specific**: The more detailed the user criteria, the better agents can filter
2. **Trust the Process**: Agents may take 2-3 minutes to complete thorough searches
3. **Review Outputs**: Each agent logs their progress for transparency
4. **Iterate**: If results aren't satisfactory, adjust search criteria and re-run

## Technical Details

**Framework:** CrewAI
**LLM Backend:** OpenAI GPT models
**Search Engine:** Serper API
**Programming Language:** Python 3.8+

## Troubleshooting

### Agent Issues

**Problem:** Agent produces no results
- Check API keys are set correctly
- Verify search criteria aren't too restrictive
- Review agent logs for errors

**Problem:** Agent takes too long
- This is normal for thorough searches (2-5 minutes)
- Ensure good internet connection
- Check API rate limits haven't been exceeded

**Problem:** Results don't match criteria
- Review the filtering logic in `src/jobcrew/tasks.py`
- Adjust task descriptions to be more specific
- Check that search tools are working correctly

## Future Enhancements

Planned agent improvements:
- Resume matching agent
- Interview preparation agent
- Salary negotiation advisor agent
- Company culture analyzer agent
- Application tracker agent

---

For more information on customizing agents and tasks, see the main README.md and review the source code in `src/jobcrew/agents.py` and `src/jobcrew/tasks.py`.
