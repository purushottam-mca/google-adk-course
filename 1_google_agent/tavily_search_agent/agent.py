from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import TavilySearch

# Create the Tavily search tool
tavily_search = TavilySearch(max_results=5, topic="general")

# Wrap it so adk can use it
tavily_search_tool = LangchainTool(
    name="tavily_search",
    description="A tool for searching the web using Tavily. Use this tool to get current information and verify facts.",
    tool=tavily_search)

# Attach to agent
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web and provide information using Tavily',
    instruction='Answer user questions to the best of your knowledge',
    tools=[tavily_search_tool]
)
