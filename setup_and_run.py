#!/usr/bin/env python3
"""
Setup script for AI Enterprise Integration Financial Intelligence Platform
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def run_streamlit():
    """Run the Streamlit app"""
    try:
        print("🚀 Starting AI Enterprise Integration Platform...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", "FFQ.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    print("🤖 AI Enterprise Integration Financial Intelligence Platform")
    print("=" * 60)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return
    
    # Install dependencies
    if install_requirements():
        print("\n🎯 Setup complete! Starting application...")
        run_streamlit()
    else:
        print("\n❌ Setup failed. Please install dependencies manually:")
        print("pip install streamlit pandas numpy plotly openpyxl xlsxwriter")

if __name__ == "__main__":
    main()