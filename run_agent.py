import asyncio
from supervisor_agent import supervisor_agent
from utils_display import format_messages
from rich.markdown import Markdown
from rich.console import Console
from langchain_core.messages import HumanMessage
from final_report import full_agent

# Example research brief for coffee shops (kept for reference)
# research_brief = """I want to identify and evaluate the coffee shops in San Francisco..."""

market_research_query = """Conduct comprehensive market research and AI/GenAI use case generation for ITC Limited. 

Your analysis should include:
1. **Industry Research**: Research ITC Limited's industry segments, market position, key offerings, and strategic focus areas
2. **Use Case Generation**: Generate relevant AI, ML, and GenAI use cases that can improve ITC's operations, customer experience, and business processes
3. **Resource Collection**: Find relevant datasets, tools, and resources from Kaggle, HuggingFace, and GitHub that support the proposed use cases
4. **Final Proposal**: Create a comprehensive proposal with prioritized use cases and clickable resource links

The final deliverable should be a professional market research report suitable for executive presentation, including:
- Industry Overview and Company Analysis
- Top AI/GenAI Use Cases ranked by priority and impact
- Resource Assets with clickable links to datasets

Focus on practical, high-impact AI solutions that align with ITC's business model and industry requirements."""

# Legacy code - using new market research system instead

async def main():
    console = Console()
    
    console.print("\n🚀 Starting Market Research & Use Case Generation for ITC Limited...", style="bold blue")
    console.print("This comprehensive analysis will include industry research, AI use case generation, resource collection, and final proposal synthesis.\n")
    
    # Execute the market research process

    thread = {"configurable": {"thread_id": "1", "recursion_limit": 50}}

    result = await full_agent.ainvoke({"messages": [HumanMessage(content=market_research_query)]}, config=thread)
    format_messages(result['messages'])

    Markdown(result["final_report"])
    
    console.print("\n✅ Market Research & Use Case Generation Complete!", style="bold green")



if __name__ == "__main__":
    asyncio.run(main())