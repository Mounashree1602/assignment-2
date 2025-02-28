# CDP Chatbot

## Overview
The **CDP Chatbot** is an AI-powered chatbot designed to answer questions related to four Customer Data Platforms (CDPs): **Segment, mParticle, Lytics, and Zeotap**. It extracts relevant information from official documentation and provides guidance on various tasks within each platform.

## Features
- **Answer "How-to" Questions**: Provides step-by-step guidance for performing tasks in Segment, mParticle, Lytics, and Zeotap.
- **Documentation Extraction**: Retrieves relevant information from the official documentation of each CDP.
- **Cross-CDP Comparisons**: Explains the differences between the platforms.
- **Advanced Queries Handling**: Supports complex questions related to integrations, configurations, and use cases.
- **Predefined Responses**: Responds to common queries with structured answers.
- **Error Handling**: Manages errors gracefully when documentation is unavailable or processing fails.

## Prerequisites
### Install Dependencies
Ensure you have Python installed. Then, install the required libraries:
```sh
pip install openai langchain faiss-cpu
```

### Set Up OpenAI API Key
Obtain an API key from OpenAI and set it as an environment variable:
```sh
export OPENAI_API_KEY="your-api-key-here"  # For Mac/Linux
set OPENAI_API_KEY="your-api-key-here"  # For Windows
```
Alternatively, you can set it directly in the script:
```python
import openai
openai.api_key = "your-api-key-here"
```

## Usage
### Run the Chatbot
Execute the script using:
```sh
python cdp_chatbot.py
```
The chatbot will start, and you can ask questions such as:
- "How do I set up a new source in Segment?"
- "How can I create a user profile in mParticle?"
- "How do I build an audience segment in Lytics?"
- "How can I integrate my data with Zeotap?"

To exit, type `exit`, `quit`, or `bye`.

## Structure
- **cdp_chatbot.py**: Main chatbot script.
- **README.md**: Documentation for setup and usage.

## Future Enhancements
- Add support for more CDPs.
- Improve NLP capabilities for better query understanding.
- Implement a web-based interface.




