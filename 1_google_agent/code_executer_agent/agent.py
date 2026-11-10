from google.adk.agents.llm_agent import Agent
from google.adk.code_executors import BuiltinCodeExecuter

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can write and execute code in Python',
    instruction='Answer user questions accurately and provide helpful code execution assistance. If you need to execute code, use the code_executer_agent.',
    code_executer_agent=BuiltinCodeExecuter()
)
