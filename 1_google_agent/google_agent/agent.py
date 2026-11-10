from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction='Answer user questions procesly and accurately. If you need current information or need to verify facts then use the google_search tool.',
    tools=[google_search],
)
