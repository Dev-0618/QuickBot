# QuickBot

**QuickBot** is a Python-based chatbot designed to answer Python-related queries, fetch Google search results, perform website cloning using `curl`, and utilize Google Dorking techniques to retrieve specific file types from a given domain. QuickBot leverages Natural Language Processing (NLP) for responding intelligently to user queries and offers various features for developers and cybersecurity enthusiasts.

## Features
- **NLP-based chatbot** for Python and general queries.
- Fetches Google search results directly in the chat.
- Website cloning using the `curl` command.
- Google Dorking to search for specific file types on a domain.
- Simple interface with usage commands for ease of use.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Dev-0618/QuickBot/
cd QuickBot
pip install -r requirements.txt
python quickbot.py
```

## Usage

1. **Start the bot**:
   Once you've installed the required modules and run the script, the chatbot will be available to interact with.

2.- **Usage Command**:
     ```bash
     usage
     ```
     Response: Provides details on how to use the chatbot with different functionalities.
 

3. **Example queries**:
   - **Basic conversation**:
     ```bash
     hello
     ```
     
   - **Ask Python-related queries or about py-modules**:
     ```bash
     what is python? #not just this you can ask any python modules with it
     ```
     Expected Response: "Python is a high-level, interpreted, interactive, and object-oriented scripting programming language."

   - **Search on Google**:
     ```bash
     google: artificial intelligence
     ```
     Response: Google search results will be fetched and displayed directly in the chat.

   - **Clone a website** using `curl`:
     ```bash
     curl: https://example.com
     ```
     Response: The website will be cloned and saved as `index.html`.

   - **Perform Google Dorking**:
     ```bash
     extract: drive.google.com .pdf networking
     ```
     Response: Displays results for PDF files on Google Drive related to "networking."

  ## License

This project is licensed under the MIT License.
