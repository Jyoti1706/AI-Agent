"""
It has multiple agent

PS: 1. Summarize and recommend stock of NVIDIA
Agent 1: Interact to get details of stock
Agent 2: News Information

"""

from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")


websearch_agent = Agent(
    name = "web Search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include the sources"],
    show_tools_calls = True,
    markdown = True
)

## Finance Agent 

finance_agent = Agent(
    name = "Fianance Agent",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
           ],
    instructions = ["Use Table to Display Data"],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent = Agent(
    team = [websearch_agent, finance_agent],
    instructions = ["Always include the sources","Use Table to Display Data"],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA")