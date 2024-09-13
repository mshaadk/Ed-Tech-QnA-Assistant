# Ed-Tech QnA Assistant
This project leverages LangChain, FAISS, and Groq to create an intelligent assistant capable of answering questions based on a knowledge base built from a CSV file.

## Overview
This project uses a combination of advanced language models and vector stores to provide contextually accurate answers to user queries. This is achieved through a two-step process:

1. **Building a Vector Database**: Converts a CSV file containing FAQs into a vector database using FAISS for efficient similarity search.
2. **Querying the Knowledge Base**: Utilizes a language model and a custom prompt to generate accurate responses based on the context retrieved from the vector database.

## Features
- **CSV Loader**: Load FAQs from a CSV file.
- **Vector Database**: Use FAISS for storing and querying documents efficiently.
- **Custom Prompting**: Generate contextually accurate answers using a custom prompt template.
- **Groq Integration**: Utilize the Groq API for advanced language model capabilities.
- **Streamlit Interface**: Simple web interface for interacting with the assistant.
  
## Installation
### 1.Clone the repository:

```bash
git clone https://github.com/mshaadk/Ed-Tech-QnA-Assistant.git
cd Ed-Tech-QnA-Assistant
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables: 
Create a `.env` file in the root directory of the project and add your Groq API key:

```plaintext
GROQ_API_KEY=your_groq_api_key
```

## Usage
### Create Vector Database
To create the vector database from the CSV file, run the following command:

```bash
streamlit run main.py
```
Upload the CSV file and Click 'Create Knowledgebase'. This will create a knowledge base and you can ask questions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing
Feel free to open issues and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any questions or feedback, please reach out to [Mohamed Shaad](https://www.linkedin.com/in/mohamedshaad/).

