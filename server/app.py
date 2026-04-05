from fastapi import FastAPI
from app.env import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.get("/")
def root():
    return {"message": "Email Env Running"}

@app.get("/")
def home():
    return {"message": "Email Triage Environment Running"}

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()