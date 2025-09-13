from typing_extensions import Annotated, Literal
from pydantic import BaseModel, Field
from langchain_core.tools import tool, InjectedToolArg
from utils_agent import (
    tavily_search_multiple,
    deduplicate_search_results,
    process_search_results,
    format_search_output,
)

# ===== RESEARCH TOOLS =====

@tool(parse_docstring=True)
def tavily_search(
    query: str,
    max_results: Annotated[int, InjectedToolArg] = 3,
    topic: Annotated[Literal["general", "news", "finance"], InjectedToolArg] = "general",
) -> str:
    """Fetch results from Tavily search API with content summarization.

    Args:
        query: A single search query to execute
        max_results: Maximum number of results to return
        topic: Topic to filter results by ('general', 'news', 'finance')

    """
    # Execute search for single query
    search_results = tavily_search_multiple(
        [query],  # Convert single query to list for the internal function
        max_results=max_results,
        topic=topic,
        include_raw_content=True,
    )

    # Deduplicate results by URL to avoid processing duplicate content
    unique_results = deduplicate_search_results(search_results)

    # Process results with summarization
    summarized_results = process_search_results(unique_results)

    # Format output for consumption
    return format_search_output(summarized_results)

@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """Tool for strategic reflection on research progress and decision-making.
    
    Use this tool after each search to analyze results and plan next steps systematically.
    This creates a deliberate pause in the research workflow for quality decision-making.
    
    When to use:
    - After receiving search results: What key information did I find?
    - Before deciding next steps: Do I have enough to answer comprehensively?
    - When assessing research gaps: What specific information am I still missing?
    - Before concluding research: Can I provide a complete answer now?
    
    Reflection should address:
    1. Analysis of current findings - What concrete information have I gathered?
    2. Gap assessment - What crucial information is still missing?
    3. Quality evaluation - Do I have sufficient evidence/examples for a good answer?
    4. Strategic decision - Should I continue searching or provide my answer?
    
    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps

    """
    return f"Reflection recorded: {reflection}"

# ---- Supervisor Layer Tools ----

@tool
class ConductResearch(BaseModel):
    """Tool for delegating a research task to a specialized sub-agent."""
    research_topic: str = Field(
        description="The topic to research. Should be a single topic, and should be described in high detail (at least a paragraph).",
    )

@tool
class ResearchComplete(BaseModel):
    """Tool for indicating that the research process is complete."""
    pass

# ---- Market Research Specialized Tools ----

@tool
class IndustryResearch(BaseModel):
    """Tool for delegating industry and company research to a specialized agent."""
    company_or_industry: str = Field(
        description="The company name or industry to research. Should include specific details about what aspects to focus on.",
    )

@tool
class UseCaseGeneration(BaseModel):
    """Tool for generating AI/GenAI use cases based on industry research."""
    industry_context: str = Field(
        description="The industry context and company information to generate use cases for. Should be detailed.",
    )

@tool
class ResourceCollection(BaseModel):
    """Tool for collecting datasets and resources from Kaggle, HuggingFace, and GitHub."""
    use_cases: str = Field(
        description="The use cases to find relevant datasets and resources for. Should be specific.",
    )

@tool
class FinalProposal(BaseModel):
    """Tool for generating the final comprehensive proposal with top use cases."""
    all_research_data: str = Field(
        description="All collected research data including industry info, use cases, and resources.",
    )

@tool(parse_docstring=True)
def search_datasets(
    query: str,
    platforms: Annotated[list[str], InjectedToolArg] = ["kaggle", "huggingface", "github"],
) -> str:
    """Search for relevant datasets and resources on specified platforms.

    Args:
        query: Search query for datasets related to specific use cases
        platforms: List of platforms to search on ('kaggle', 'huggingface', 'github')

    """
    results = []
    
    for platform in platforms:
        if platform.lower() == "kaggle":
            # Search Kaggle datasets
            search_query = f"site:kaggle.com/datasets {query} machine learning dataset"
        elif platform.lower() == "huggingface":
            # Search HuggingFace datasets
            search_query = f"site:huggingface.co/datasets {query} dataset"
        elif platform.lower() == "github":
            # Search GitHub repositories
            search_query = f"site:github.com {query} dataset machine learning data"
        else:
            continue
            
        # Use existing tavily search with the constructed query
        platform_results = tavily_search_multiple(
            [search_query],
            max_results=3,
            topic="general",
            include_raw_content=True,
        )
        
        if platform_results:
            results.extend(platform_results)
    
    # Process and format results
    unique_results = deduplicate_search_results(results)
    summarized_results = process_search_results(unique_results)
    
    return f"Dataset Search Results for '{query}':\n{format_search_output(summarized_results)}"