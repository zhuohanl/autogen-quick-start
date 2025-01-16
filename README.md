This is a repo to get the AutoGen quickstart code runnable by bringing in the necessary, including:
- `.env` file
- dependencies, libraries (managed by poetry)

# How to run

Step 1: Install all the libraries
```
poetry install
```

Step 2: Update `.env` with your Azure OpenAI endpoint and deployment details
```
AZURE_OAI_ENDPOINT="xxx"
AZURE_OAI_KEY="xxx"
AZURE_OAI_DEPLOYMENT="xxx"
AZURE_OAI_MODEL="xxx"
```

Step 3: Run the script
```
poetry run python .\autogen_getting_started\run.py
```