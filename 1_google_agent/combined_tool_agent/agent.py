from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor
from google.genai import types
from langchain_tavily import TavilySearch

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# 1. 3rd party tool: Tavily search tool
tavily_search = TavilySearch(max_results=5, topic="general")

# Wrap it so adk can use it
tavily_search_tool = LangchainTool(
    name="tavily_search",
    description="A tool for searching the web using Tavily. Use this tool to get current information and verify facts.",
    tool=tavily_search)

# 2. Function tool 
def get_current_time(timezone: str) -> dict:
    """Get the current date and time in a given time zone.

    Use this whenever the user asks what time or date it is somewhere.

    Args:
        timezone: An IANA time zone name, e.g. "Asia/kolkata",, "America/New_York" or "Europe/London".
    
    Returns:
        A dict with "status" ("success" or "error"). On success it also has "timezone", "date", "time", "weekday". on Error it has "error_message".
    """
    try:
        now = datetime.now(ZoneInfo(timezone))

    except ZoneInfoNotFoundError:
        return {
            "status:" : "error",
            "error_message": f"Invalid timezone: {timezone}. Please provide a valid IANA timezone name."
        }
    return {
        "status": "success",
        "timezone": timezone,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%I:%M %p"),
        "weekday": now.strftime("%A")
    }
 
# adding multiple tools to agent
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can saerch the web, run python code and provide current time',
    instruction=(
        "Answer user questions accurately.\n"
        "- Use Google Search for current information and quick fact checks.\n"
        "- Use the Tavily search tool when you need more detailed results, "
        "multiple sources, or when Google Search did not give enough.\n"
        "- Write and run Python code for calculations or data analysis.\n"
        "- Use get_current_time whenever the user asks for the time or date "
        "somewhere. Never guess the current time.\n"
        "Cite sources when you use search results."
    ),
    tools=[google_search, tavily_search_tool, get_current_time], # built-in + third-party + function
    code_executor=BuiltInCodeExecutor(),                         # code execution goes here, not in tools
    # Below part is needed to allow server-side tool invocations, 
    # which is required for the Tavily search tool to work.
    # Here google_search and CodeExecutor are executed on googel server so adk doesn't recioved full context once they are done. 
    # Here we request the server to send the tool invocation results back to the agent so it can use them in its next response.
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(include_server_side_tool_invocations=True),
    )
)
