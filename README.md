# JobCrew 💼🤖

**Your AI-Powered Job Search Assistant**

JobCrew is an intelligent job search application that leverages the power of CrewAI and multiple specialized AI agents to find and filter the best job opportunities matching your specific criteria. Simply provide your desired position, location, salary expectations, and employment type, and let our team of AI recruitment experts handle the rest!

## 🚀 Features

- **Multi-Agent Intelligence**: Three specialized AI agents work together to find your perfect job match
- **Smart Job Search**: Uses live web search to find the latest job postings across multiple platforms
- **Intelligent Filtering**: Analyzes and filters jobs based on your exact requirements
- **Top 5 Matches**: Delivers a curated report of the 5 most promising opportunities
- **Detailed Analysis**: Provides insights on required skills, responsibilities, and company culture
- **Markdown Reports**: Automatically generates professionally formatted job reports saved as `jobs_report.md`

## 🤖 Meet Your AI Recruitment Team

### 🔍 Job Researcher Agent
- **Role**: Senior Talent Acquisition Specialist
- **Goal**: Find the most relevant and promising job opportunities online based on your specific criteria
- **Specialty**: Expert at navigating the web to unearth hidden job gems with precise search queries
- **Tools**: Advanced web search capabilities for real-time job listings

### 📊 Job Analyst Agent
- **Role**: Job Requirements and Culture Analyst
- **Goal**: Analyze each job posting to validate true matches with your requirements
- **Specialty**: Meticulous detail-oriented analyst with a sharp eye for reading between the lines
- **Filtering**: Discards any listings that don't perfectly match salary, location, and work hour requirements

### 📋 Recruitment Strategist Agent
- **Role**: Lead Recruitment Report Strategist
- **Goal**: Synthesize filtered job listings into clear, actionable reports
- **Specialty**: Transforms raw data into strategic insights that empower immediate action
- **Output**: Clean, structured reports highlighting the top 5 opportunities

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Serper API key (for web search functionality)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kutmur/JobCrew.git
   cd JobCrew
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root (use `.env.example` as template):
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

   **Getting API Keys:**
   - **OpenAI API Key**: Sign up at [OpenAI Platform](https://platform.openai.com/api-keys) and create an API key
   - **Serper API Key**: Sign up at [Serper.dev](https://serper.dev/) for web search capabilities

## 🚀 Usage

### Basic Usage

Run the application:
```bash
python main.py
```

The application will prompt you for:
- **Position**: The job title or role you're seeking (e.g., "Senior Python Developer")
- **Location**: Your preferred location or "Remote"
- **Salary Expectations**: Your desired salary range (e.g., "$80,000 - $100,000")
- **Employment Type**: Type of employment (e.g., "Full-time", "Part-time", "Contract")

### Example Session

```
======================================================================
🚀 Welcome to JobCrew - Your AI-Powered Job Search Assistant!
======================================================================

💼 Enter the position you're looking for: Senior Python Developer
📍 Enter your preferred location (or 'Remote'): Remote
💰 Enter your salary expectations (e.g., '$80,000 - $100,000'): $100,000 - $130,000
⏰ Enter employment type (e.g., 'Full-time', 'Part-time', 'Contract'): Full-time

----------------------------------------------------------------------
🔎 Searching for: Senior Python Developer
📍 Location: Remote
💰 Salary: $100,000 - $130,000
⏰ Type: Full-time
----------------------------------------------------------------------

🤖 Our AI agents are working on finding the best matches...
⏳ This may take a few minutes...
```

### Output

The application generates a comprehensive Markdown report (`jobs_report.md`) containing:

- **Executive Summary**: Overview of the job search results
- **Top 5 Job Matches**: Each with:
  - Job Title & Company Name
  - Location
  - Why it's a great match (compelling analysis)
  - Key highlights (salary, benefits, growth opportunities)
  - Direct application URL
- **Actionable Next Steps**: Recommendations for your job search

## 📁 Project Structure

```
JobCrew/
├── agents.py              # AI agent definitions (Researcher, Analyst, Strategist)
├── tasks.py               # Task definitions for the workflow
├── main.py                # Main application entry point
├── tools/
│   └── search_tools.py    # Job search tool implementation
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
├── AGENT.md              # Detailed agent documentation
└── LICENSE               # License information
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for agent intelligence | Yes |
| `SERPER_API_KEY` | Your Serper API key for web search | Yes |

### Customization

You can customize the agents and tasks by modifying:
- `agents.py`: Adjust agent roles, goals, and backstories
- `tasks.py`: Modify task descriptions and expected outputs
- `tools/search_tools.py`: Enhance search capabilities

## 🤝 How It Works

JobCrew uses a **sequential process** where agents work in order:

1. **Research Phase** 🔍
   - Job Researcher searches for relevant opportunities
   - Collects job titles, companies, locations, and URLs

2. **Analysis Phase** 📊
   - Job Analyst reviews each posting in detail
   - Filters out non-matching positions
   - Extracts key requirements and responsibilities

3. **Reporting Phase** 📋
   - Recruitment Strategist selects top 5 matches
   - Compiles professional report with insights
   - Saves output to `jobs_report.md`

## 🛡️ Best Practices

- **Be Specific**: The more detailed your criteria, the better the matches
- **Realistic Expectations**: Set achievable salary ranges based on market research
- **Location Flexibility**: Consider "Remote" or multiple locations for more opportunities
- **Review Regularly**: Job markets change quickly—run searches periodically
- **Follow Up Fast**: Apply quickly to the top matches for best results

## 🐛 Troubleshooting

### Common Issues

**Missing API Keys**
```
❌ Missing required environment variables:
   - OPENAI_API_KEY
```
**Solution**: Ensure your `.env` file exists and contains valid API keys

**No Results Found**
**Solution**: Try broadening your search criteria or adjusting salary expectations

**Rate Limits**
**Solution**: Wait a few moments between searches to avoid API rate limits

## 📝 Requirements

See `requirements.txt` for full dependency list. Key dependencies:
- `crewai>=0.28.0` - Multi-agent orchestration framework
- `crewai-tools>=0.1.6` - Search and web tools
- `python-dotenv>=1.0.0` - Environment variable management
- `langchain>=0.1.0` - LLM integration

## 🤖 Technology Stack

- **CrewAI**: Multi-agent orchestration
- **OpenAI GPT**: Agent intelligence and reasoning
- **Serper API**: Real-time web search
- **Python**: Core application language
- **Markdown**: Report formatting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI)
- Powered by [OpenAI](https://openai.com/)
- Search capabilities by [Serper](https://serper.dev/)

## 💡 Future Enhancements

- [ ] Integration with LinkedIn and Indeed APIs
- [ ] Resume matching and optimization suggestions
- [ ] Interview preparation assistance
- [ ] Salary negotiation strategies
- [ ] Company research and culture insights
- [ ] Application tracking system

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Made with ❤️ using CrewAI** | **Empowering Job Seekers with AI** 🚀
