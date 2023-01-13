# Sentiment_Analyzer_API
*Summary*

An API for sentiment analysis deployed using FastAPI. 
- *This is a great beginner's guide to anyone who wants to use FastAPI for Model Deployment.*
- *Comments are provided in a step-by-step process to make understanding much easier.*

To learn on using FastAPI visit : https://fastapi.tiangolo.com/

## Sentiment Analyzer API

- This API uses vaderSentiment to perform sentiment analysis on text input. 
- It is built using FastAPI, pydantic's BaseModel for data validation and can be accessed using uvicorn. 
- The API also contains a Dockerfile, which can be used to build and run the API in a container.

### Installation
- Clone the repository to your local machine.
- Create *a virtual environment and activate it.
- Run `pip install -r requirements.txt` to install the necessary packages.

### Usage
- Start the server by running `uvicorn app:api --reload` in the terminal.
- Add `/docs` to the url to see the automatic interactive API documentation by SwaggerUI that is present when using FastAPI.

### Notes
- Sentiment can be either "positive", "negative" or "neutral"
- Compound Score is a value between -1 and 1, indicating the sentiment analysis.

## Deployment
- To deploy the API in production, you can use the attached Dockerfile to build an image.
- The Dockerfile uses `python:3.9-slim` as the base image, and sets the working directory to `/api`.
- It copies the `requirements.txt` file and runs `pip install` to install the necessary packages.
- It also copies all the files from the current directory to `/api`
- Finally, the CMD instruction runs uvicorn to start the API on `127.0.0.1:8000`

You can also use a container orchestration tool like Kubernetes to manage the containers in a production environment.
