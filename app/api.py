from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils import agent_app
import uvicorn

app = FastAPI(title="CollegeInfoBot API")

class ChatRequest(BaseModel):
    message: str

@app.post("/run-agent")
async def run_agent(request: ChatRequest):
    # Mapping the UI message to the Agent's expected 'user_input' key
    initial_state = {
        "user_input": request.message,
        "university": None,
        "program": None,
        "status": "started"
    }
    
    try: 
        print(f"DEBUG: API received: {request.message}")
        
        # FIX: Use .ainvoke() instead of .invoke()
        final_state = await agent_app.ainvoke(initial_state)
        
        print(f"DEBUG: Agent extracted: {final_state.get('university')}")
        return final_state
        
    except Exception as e:
        # This will print the error to your terminal so you can see it
        print(f"ERROR: {str(e)}") 
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="127.0.0.1", port=8001, reload=True)