# creating Python API with FastAPi

from fastapi import FastAPI


app = FastAPI()

# basic root 
@app.get("/")
def read():
    return { "hello": "world!"}


if__name__== "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
