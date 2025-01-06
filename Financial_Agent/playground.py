from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app


load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.environ["PHI_API_KEY"]=os.getenv("PHI_API_KEY")



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
    instructions = ["Always include the sources","Use Table to Display Data"],
    show_tools_calls = True,
    markdown = True,
)


app = Playground(agents=[finance_agent, websearch_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)