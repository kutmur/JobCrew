#!/usr/bin/env python3
"""
JobCrew Application Entry Point
Wrapper script to run the JobCrew application from the root directory.
"""

import sys
import os

# Add src directory to Python path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main function
from jobcrew.main import main

if __name__ == "__main__":
    main()
