# Pydantic model.
from pydantic import BaseModel
from typing import Optional, TypedDict

class ChatRequest(BaseModel):
    message: str

class ResearchRequest(BaseModel):
    university: str
    program: str
    level: str
    background: Optional[str]=None

class AgentState(TypedDict):
    user_input: str
    university: Optional[str]
    program: Optional[str]
    level: Optional[str]      
    background: Optional[str] 
    status: str