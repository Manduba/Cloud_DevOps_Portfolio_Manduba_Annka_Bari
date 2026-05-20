from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

top = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canario Prototype</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding: 20px;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
        }
        footer {
            margin-top: 20px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Canario:MYTEST</h1>
    </header>
    <h2>This website is for Trump</h2>
    <ul>
        <li>Meet Your Friend Trump</li>
        <li>Great speeker</li>
        <li>Great Humor</li>
    </ul>
'''

feature = '''<h2>Proposed Business</h2>
    <ul>
        <li>Making Profit</li>
        <li>Doing politics</li>
        <li>Drama king</li>
    </ul>
'''

tail = '''    <footer>
        <p>&copy; 2024 Canario Project</p>
    </footer>
</body>
</html>
'''

@app.get("/", response_class=HTMLResponse)
async def read_root():
    GET_LEVEL = os.environ.get('GET_LEVEL')
    if GET_LEVEL == "1":
        return top+feature+tail
    else:
        return top+tail


# To run FastAPI: pip install fastapi uvicorn
# Run the app: uvicorn main:app --host 0.0.0.0 --port 8000