import streamlit as st
import asyncio
import re
from datetime import datetime

# Import your existing agent modules
from final_report import full_agent
from langchain_core.messages import HumanMessage

# ===== STREAMLIT CONFIGURATION =====
st.set_page_config(
    page_title="Market Research & AI Use Case Generator",
    page_icon="🔍",
    layout="wide"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 1.5rem;
    }
    
    .output-panel {
        border: 2px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        background: #f8f9fa;
        min-height: 500px;
    }
    
    .resource-link {
        color: #007bff;
        text-decoration: none;
        font-weight: 500;
    }
    
    .resource-link:hover {
        color: #0056b3;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# ===== SESSION STATE INITIALIZATION =====
if 'research_results' not in st.session_state:
    st.session_state.research_results = None
if 'research_in_progress' not in st.session_state:
    st.session_state.research_in_progress = False

# ===== UTILITY FUNCTIONS =====

def extract_clickable_links(text: str) -> str:
    """Convert URLs in text to clickable markdown links"""
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    
    def replace_url(match):
        url = match.group(0)
        display_url = url if len(url) <= 60 else url[:57] + "..."
        return f'<a href="{url}" target="_blank" class="resource-link">{display_url}</a>'
    
    return re.sub(url_pattern, replace_url, text)

# ===== MAIN RESEARCH FUNCTION =====

async def run_research(query: str):
    """Run the research process"""
    try:
        st.session_state.research_in_progress = True
        
        # Create thread configuration
        thread = {"configurable": {"thread_id": "streamlit_session", "recursion_limit": 50}}
        
        # Run the research
        result = await full_agent.ainvoke(
            {"messages": [HumanMessage(content=query)]}, 
            config=thread
        )
        
        # Store results
        st.session_state.research_results = result
        st.session_state.research_in_progress = False
        
        return result
        
    except Exception as e:
        st.error(f"Research failed: {str(e)}")
        st.session_state.research_in_progress = False
        return None

# ===== MAIN APP =====

def main():
    """Main Streamlit application"""
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔍 Market Research & AI Use Case Generator</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Main layout: Left (Input) and Right (Output) in 1:3 ratio
    col1, col2 = st.columns([1, 3])
    
    # Left Column - Input Panel
    with col1:
        # Text input area
        query = st.text_area(
            "Research Query:",
            placeholder="Enter your research query here...",
            height=400,
            key="query_input"
        )
        
        # Button row
        if st.button("Start Research", type="primary", use_container_width=True):
            if query.strip():
                asyncio.run(run_research(query))
                st.rerun()
            else:
                st.error("Please enter a research query first.")
        
        if st.session_state.research_results and 'final_report' in st.session_state.research_results:
            report = st.session_state.research_results['final_report']
            st.download_button(
                label="Download",
                data=report,
                file_name=f"market_research_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        else:
            st.button("Download", disabled=True, use_container_width=True)
        
        if st.session_state.research_results:
            if st.button("New Research", use_container_width=True):
                st.session_state.research_results = None
                st.session_state.research_in_progress = False
                st.rerun()
        else:
            st.button("New Research", disabled=True, use_container_width=True)
    
    # Right Column - Output Panel
    with col2:
        st.markdown('<div class="output-panel">', unsafe_allow_html=True)
        
        if st.session_state.research_results and 'final_report' in st.session_state.research_results:
            # Display the report with clickable links
            report = st.session_state.research_results['final_report']
            report_with_links = extract_clickable_links(report)
            st.markdown(report_with_links, unsafe_allow_html=True)
        elif st.session_state.research_in_progress:
            st.info("🔄 Research in progress...")
        else:
            st.info("Enter a research query to begin.")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
