from google.adk.agents.llm_agent import Agent

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# # Create the Tavily search tool
# tavily_search = TavilySearch(max_results=5, topic="general")

# # Wrap it so adk can use it
# tavily_search_tool = LangchainTool(
#     name="tavily_search",
#     description="A tool for searching the web using Tavily. Use this tool to get current information and verify facts.",
#     tool=tavily_search)

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

# Attach to agent
root_agent = Agent(
    model='gemini-3.5-flash',
    name='clock_agent',
    description='A helpful assistant that can provide current time in various city or country',
    instruction="Change the places name into IANA time zones yourself (e.g. Delhi -> Asia/Kolkata) and call get_current_time." "" \
    "If it returns Erro rthen exp;lain the problem and ask the user to provide a valid IANA timezone name.",
    tools=[get_current_time]
)
