#!/usr/bin/env python3
"""FastAPI server wrapper for Open Interpreter"""

import os
import subprocess
import tempfile
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="Open Interpreter API")

LLM_API_URL = os.environ.get("LLM_API_URL", "http://localhost:8000")
DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


class ChatRequest(BaseModel):
    message: str
    stream: bool = True


@app.get("/health")
def health():
    return {"status": "ok", "llm_url": LLM_API_URL}


@app.post("/chat")
def chat(req: ChatRequest):
    """Run Open Interpreter with a message and return output."""
    
    # Create a temp script that runs interpreter with the message
    script = f"""
import sys
sys.path.insert(0, '/usr/local/lib/python3.12/site-packages')
from interpreter import interpreter

interpreter.llm.model = "openai/x"
interpreter.llm.api_key = "fake_key"
interpreter.llm.api_base = "{LLM_API_URL}"
interpreter.auto_run = True
interpreter.offline = True

# Run the message
result = interpreter.chat("{req.message.replace(chr(34), chr(92) + chr(34))}", stream={str(req.stream).lower()})

# Print result
if isinstance(result, list):
    for msg in result:
        print(f"RESULT: {{msg}}")
else:
    print(f"RESULT: {{result}}")
"""
    
    # Write script to temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(script)
        script_path = f.name
    
    try:
        # Run the script
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail=f"Interpreter error: {result.stderr}"
            )
        
        return {"output": result.stdout}
        
    finally:
        os.unlink(script_path)


@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    """Stream Open Interpreter output."""
    
    script = f"""
import sys
sys.path.insert(0, '/usr/local/lib/python3.12/site-packages')
from interpreter import interpreter

interpreter.llm.model = "openai/x"
interpreter.llm.api_key = "fake_key"
interpreter.llm.api_base = "{LLM_API_URL}"
interpreter.auto_run = True
interpreter.offline = True

for chunk in interpreter.chat("{req.message.replace(chr(34), chr(92) + chr(34))}", stream=True):
    print(f"SSE: {{chunk}}", flush=True)
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(script)
        script_path = f.name
    
    try:
        def generate():
            proc = subprocess.Popen(
                ["python", script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            for line in proc.stdout:
                if line.startswith("SSE: "):
                    yield f"data: {line[5:]}\\n\\n"
            
            proc.wait()
        
        return StreamingResponse(generate(), media_type="text/event-stream")
        
    finally:
        os.unlink(script_path)


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
