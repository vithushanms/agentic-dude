# agentic-dude

Agentic-dude is a project includes an LLM based agentic RAG which leverage various dudes aka tools. This has various tools like summarization, question answering, etc.
</br>
</br>
Current version supports CLI based question answering and summarization.

## Features

Dude comes with following features:

- Answer the questions based on the pdf
- Summarize the pdf
- Take the bullet points of the pdf and generte a short summary material

## Technologies used

- transformer based LLM models
- llamaindex
- python3 runtime

## Get started

1. Create a virtual environment

```
python3 -m venv agentic-dude
```

2. Activate the virtual environment

```
source ./agentic-dude/bin/activate
```

3. Install the dependencies

```
pip3 install -r requirements.txt
```

4. We are using OpenAI models. Therefore, create an OpenAI api key and add it the .env variable as per the .env.example file.

5. Run the agentic-dude

```
cd src
python3 main.py
```
