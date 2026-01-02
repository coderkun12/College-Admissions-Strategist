import os
from typing import TypedDict, Optional
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv
load_dotenv()
"""
Defining a LLM and a API which will help the UI to have a file name based on the University name and program name. 
LLM is tasked only to extract the university name and program name and return it as a JSON output to the ui.py file.
"""

class AgentState(TypedDict):
    user_input:str
    university:Optional[str]
    program:Optional[str]
    status:str

llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0,
               groq_api_key=os.getenv("GROQ_API_KEY"))

# Defining a extraction node. 
async def extraction_node(state: AgentState):
    """
    This worker only cares about finding the Uni and Program name.
    """
    prompt=ChatPromptTemplate.from_template("Extract the university and program from this text:{text}"
                                            "Return ONLY a JSON with 'university' and 'program' keys.")
    chain=prompt|llm|JsonOutputParser()
    result=await chain.ainvoke({"text":state["user_input"]})
    return{
        "university":result.get("university"),
        "program":result.get("program"),
        "status":"extraction_complete"
    }
workflow=StateGraph(AgentState)
workflow.add_node("extractor",extraction_node)
workflow.set_entry_point("extractor")
workflow.add_edge("extractor",END)

agent_app=workflow.compile()


# import asyncio

# async def test_agent():
#     print("--- Testing Agent Extraction ---")
#     test_input = {"user_input": "I want to apply for the Computer Science program at Stanford University."}
    
#     try:
#         # We call the compiled agent directly
#         result = await agent_app.ainvoke(test_input)
#         print("SUCCESS!")
#         print(f"Result: {result}")
#     except Exception as e:
#         print("FAILED!")
#         # This will print the full technical error (Traceback)
#         import traceback
#         traceback.print_exc()

# if __name__ == "__main__":
#     # This runs the async test function
#     asyncio.run(test_agent())