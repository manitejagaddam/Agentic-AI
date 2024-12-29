from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os 
import phi.api 


load_dotenv()


pdf_analyser = Agent(
    name = "Pdf Analyser Agent",
    role = "Extraxts the information from the pdf and stores it in Data Base",
    model = Groq(id = "llama-3.1-70b-versatile"),
    tools = [],
    instructions=["Extract all the required information from pdf and store it in an point wise in the database"],
    show_tool_calls=True,
    markdown=True,
)


