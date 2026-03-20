# P&G AI developer Technical Task
## *Archan Tulpule*

### Task Description
This repository provides an LLM-driven data-extraction pipeline that captures product information in JSON format from product promotional text. 

### Repository Structure

The repository is divided into the following folders:
- **inputs**: for .txt input files that contain promotional product paragraphs
- **outputs**: for .json outputs to be stored after data extraction and valdiation
- **src**: contains all of the exraction and validation code and scripts as an importable module
- **tests**: the suite of test cases for schema validation, prompt creation, and pipeline processing

### Reproducability Steps
1. Create virtual environment: `python3 -m venv pg-task`
2. Activate virtual environment: `source pg-task/bin/activate`
3. Create environment variable file: `touch .env`
4. Add Gemini API Key to .env file: `GEMINI_API_KEY=<INSERT API KEY HERE>`
5. Update PYTHONPATH for tests: `export PYTHONPATH="$PYTHONPATH:$PWD"`

