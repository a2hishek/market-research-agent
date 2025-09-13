#!/usr/bin/env python3
"""
Streamlit App Launcher for Market Research Agent

This script launches the Streamlit UI for the Market Research & AI Use Case Generator.
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import langchain
        import langgraph
        print("✅ All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def launch_streamlit():
    """Launch the Streamlit application"""
    if not check_dependencies():
        return
    
    print("🚀 Launching Market Research Agent UI...")
    print("📱 The app will open in your default web browser")
    print("🔗 If it doesn't open automatically, go to: http://localhost:8501")
    print("\n" + "="*50)
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Streamlit app stopped by user")
    except Exception as e:
        print(f"❌ Error launching Streamlit: {e}")

if __name__ == "__main__":
    launch_streamlit()
