from fastapi import FastAPI
from utils import HelloWorld  # Import the HelloWorld class from utils.py

# Read the config.yaml file
import yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract ports and title from the config file
http_port = config["ports"]["http"]
websocket_port = config["ports"]["websocket"]
title = config["title"]

# Create the FastAPI app
app = FastAPI(title=title)

# Create an instance of the HelloWorld class
hello_world_instance = HelloWorld()

# GET request to read two inputs from query parameters
@app.get("/zero_shot")
def zero_shot(CGPA: int, IQ: int):
    return {"message": hello_world_instance.zero_shot(CGPA, IQ)}

# Run the Uvicorn server with the specified port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=http_port)
