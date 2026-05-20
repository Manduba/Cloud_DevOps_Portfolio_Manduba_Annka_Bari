# 1. Use Python as the base image
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy all files from your current directory on your computer to the /app directory in the container
COPY . .

# 4. Install FastAPI and Uvicorn (used to run FastAPI applications)
RUN pip install fastapi uvicorn

# 5. Expose the port that FastAPI will run on (usually 8000)
EXPOSE 8000

# 6. Command to run your FastAPI application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

