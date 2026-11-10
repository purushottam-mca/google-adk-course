## Steps to create

- Create folder and open inside VS Code 
- Create virtual env - python3 -m venv .venv 
- Activate - source .venv/bin/activate  
- Install google adk - pip install google-adk 
- adk command -> Check adk version - adk --version 
- Create agent project - adk create helloWorldAgent 
- Get Gemini API key 

## How to run
- Run the agent - adk run helloWorldAgent 
- Run the web interface - adk web
- Run the api service - adk api_server 

## Other Models
### LiteLLM is a library that lets your code talk to 100+ LLM providers (OpenAI, Anthropic, Ollama and more) through one standard interface, so switching models is a one-line change
- Run with other models 
- pip install litellm 

- Add -> model=LiteLlm(model="openai/gpt-4o") 
- Get openai api key and add to .env 

- Add model config  

    generate_content_config=types.GenerateContentConfig(  
        temperature=0.3, # lower = more consistent support answers 
        max_output_tokens=800 
    ) 