# 🔍 Market Research & AI Use Case Generator

A sophisticated multi-agent system that generates comprehensive AI/ML use cases for companies and industries, featuring both a command-line interface and a modern Streamlit web UI.

## Streamlit UI
<img width="1745" height="843" alt="image" src="https://github.com/user-attachments/assets/130af96e-fda7-4779-9684-9812ff8c344d" />


## 🎯 Overview

This project provides an intelligent market research solution that:
- Conducts deep industry and company analysis
- Generates relevant AI/ML use cases tailored to specific business needs
- Collects datasets and resources from Kaggle, HuggingFace, and GitHub
- Delivers executive-ready reports with clickable resource links

## 🏗️ Architecture

### Multi-Agent System
- **Research Agent**: Conducts web research using Tavily search API
- **Supervisor Agent**: Coordinates multiple research agents and manages workflow
- **Final Report Generator**: Synthesizes findings into comprehensive reports
- **Research Brief Generator**: Creates structured research briefs from user queries

### Technology Stack
- **Backend**: Python, LangChain, LangGraph
- **AI Models**: Google Gemini 2.5 Flash
- **Web Search**: Tavily Search API
- **Frontend**: Streamlit
- **Data Processing**: Pydantic, Rich (for CLI display)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API Keys:
  - `TAVILY_API_KEY` - For web search functionality
  - `GOOGLE_API_KEY` - For Google Gemini models

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/a2hishek/market-research-agent.git
   cd market-research-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example config
   cp config_example.env .env
   
   # Edit .env with your API keys
   TAVILY_API_KEY=your_tavily_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🖥️ Usage

### Option 1: Streamlit Web UI (Recommended)

Launch the modern web interface:

```bash
# Using the launcher script
python run_streamlit.py

# Or directly with Streamlit
streamlit run streamlit_app.py
```

**Features:**
- Clean, minimal interface with 1:3 layout ratio
- Real-time research progress tracking
- Clickable resource links
- Download reports as Markdown files
- Responsive design

### Option 2: Command Line Interface

Run the agent directly from the command line:

```bash
python run_agent.py
```

**Features:**
- Rich console output with formatted messages
- Detailed research process logging
- Professional report generation

## 📝 Example Queries

```
Conduct comprehensive market research and AI/GenAI use case generation for Tesla Inc.

Analyze Microsoft Corporation and generate AI use cases for their cloud services division.

Research the healthcare industry and propose AI solutions for patient care optimization.

Study the retail sector and identify AI opportunities for supply chain management.
```

## 📊 Output Features

### Research Reports Include:
- **Industry Overview**: Market analysis and company positioning
- **AI Use Cases**: Prioritized recommendations with implementation details
- **Resource Assets**: Direct links to relevant datasets and tools
- **Implementation Guidance**: Technical requirements and next steps

### Resource Integration:
- **Kaggle Datasets**: Machine learning datasets and competitions
- **HuggingFace Models**: Pre-trained models and datasets
- **GitHub Repositories**: Open-source tools and implementations
- **Research Papers**: Academic references and industry reports

## 🎨 UI Screenshots

### Streamlit Interface
- **Left Panel**: Query input and action buttons
- **Right Panel**: Scrollable research report with clickable links
- **Clean Design**: Minimal, professional interface

## 🔧 Configuration

### Environment Variables
```bash
# Required
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_api_key

# Optional
MAX_RESEARCH_ITERATIONS=6
MAX_CONCURRENT_RESEARCHERS=2
```

### Customization Options
- Adjust research depth by modifying iteration limits
- Configure concurrent research agents
- Customize report templates and formatting
- Add new data sources and search platforms

## 📁 Project Structure

```
MarketResearchAgent/
├── agent.py                 # Research agent implementation
├── supervisor_agent.py      # Multi-agent coordination
├── final_report.py         # Report generation system
├── reserach_brief.py       # Research brief creation
├── tools.py                # Search and utility tools
├── state.py                # State management
├── schema.py               # Data schemas
├── prompts.py              # AI prompts and templates
├── utils_agent.py          # Agent utilities
├── utils_display.py        # Display utilities
├── streamlit_app.py        # Streamlit web UI
├── run_streamlit.py        # UI launcher
├── run_agent.py            # CLI launcher
├── requirements.txt        # Python dependencies
├── config_example.env      # Environment template
├── README.md               # This file
```

## 🛠️ Development

### Adding New Features
1. **New Search Sources**: Extend `tools.py` with additional search APIs
2. **Custom Report Formats**: Modify `final_report.py` for different output styles
3. **UI Enhancements**: Update `streamlit_app.py` for new interface features
4. **Agent Capabilities**: Extend agent prompts in `prompts.py`

### Testing
```bash
# Test the CLI version
python run_agent.py

# Test the Streamlit UI
streamlit run streamlit_app.py
```

## 🔍 API Integration

### Tavily Search API
- Web search and content extraction
- Real-time information gathering
- Content summarization

### Google Gemini API
- Advanced language model capabilities
- Multi-agent coordination
- Report generation and synthesis

## 📈 Performance

- **Research Speed**: 2-5 minutes for comprehensive analysis
- **Concurrent Processing**: Multiple research agents working in parallel
- **Resource Efficiency**: Optimized API usage and caching
- **Scalability**: Configurable limits and resource management

## 🙏 Acknowledgments

- **LangChain**: Multi-agent framework
- **Streamlit**: Web UI framework
- **Google Gemini**: AI language models
- **Tavily**: Web search API
- **Rich**: Beautiful terminal output

---

