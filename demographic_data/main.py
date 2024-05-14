# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.demographic_data_analyzer()

# Run unit tests automatically
main(module='test', exit=False)