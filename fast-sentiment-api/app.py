# Step by Step Guide to Deployment using FastAPI

import uvicorn                           # import uvicorn to run the API locally on our machine and test it. It is a lightning-fast ASGI server implementation. 

from fastapi import FastAPI              # import FastAPI to create an API. 
# It is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

from pydantic import BaseModel           # import BaseModel from pydantic to create a model for the data we will be passing to the API. 
 # It will be used to validate the data. i.e. it will check if the data is of the correct type and format.

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# It is used to perform sentiment analysis on the text data.
# It is a lexicon and rule-based sentiment analysis tool that is used to perform sentiment analysis on social media platforms. It is specifically attuned to sentiments expressed in social media.


api = FastAPI(title="Fast_Sentiment - Sentimental Analyzer API")
# Create an 'api' instance of the FastAPI class.
# The title parameter is used to set the title of the API. 


class UserInput(BaseModel):
    text: str
# Create a class called UserInput that inherits from the BaseModel class.
# The text parameter is used to set the type of the data that will be passed to the API. In this case, it is a string.
#  So, the API will only accept string data.


@api.get("/")                          # Write a path operation decorator(like: @app.get('/'). @api.get('/') means that the API will only accept GET requests.
def home():
    return {"Message": "Welcome to Fast_Sentiment!"}
# Write a path operation function, in this case, it is a function that returns a dictionary.
# The function is called home and it returns a dictionary with a key called Message and a value called Welcome to Fast_Sentiment!.


@api.post("/sentiment")                # Write a path operation decorator(like: @app.get('/'). @api.post('/sentiment') means that the API will only accept POST requests.
async def get_sentiment(input : UserInput):  # Define a function called get_sentiment that takes a parameter called input and it is of type UserInput which is the class we created above.
    analyzer = SentimentIntensityAnalyzer()  # Create an instance of the SentimentIntensityAnalyzer class.
    result = analyzer.polarity_scores(input.text) # Create a variable called result and assign it the value of the polarity_scores method of the SentimentIntensityAnalyzer class.
    # The polarity_scores method takes a parameter called input.text which is the text data that will be passed to the API.
    
    sentiment = None                  # Create a variable called sentiment and assign it the value of None.
    if result["compound"] >= 0.05:    # If the compound score is greater than or equal to 0.05, then the sentiment is positive.
        sentiment = "Positive"
    elif result["compound"] <= -0.05: # If the compound score is less than or equal to -0.05, then the sentiment is negative.
        sentiment = "Negative"
    else:
        sentiment = "Neutral"         # If the compound score is between -0.05 and 0.05, then the sentiment is neutral.


    ''' 
     The compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1(most extreme positive).
     The compound score is also known as the sentiment score.
     Each lexicon rating is a number between -1 and 1. For example, the lexicon rating for the word 'good' is 0.34. It can also be negative, for example, the lexicon rating for the word 'bad' is -0.34.
     The compound score is the sum of all the lexicon ratings for each word in the text divided by the number of words in the text.
     For example, if the text is 'Today is a good day' then the compound score is 0.34/4 = 0.085, which is a positive sentiment. 
    '''
    return f"The sentiment of the text is {sentiment} and the Compound Score is {result['compound']}"
# Finally, we return a string that contains the sentiment of the text and the compound score of the text. 2 is the number of decimal places we want to round the compound score to.


# Now, run the API
if __name__ == "__main__":            
    uvicorn.run(api, host="127.0.0.1", port=8000) # Run the API on the local machine and set the host to 8000. The host is the IP address of the machine where the API is running. The port is the port number on which the API is running.

# Now, run the API by typing the following command in the terminal: uvicorn app:api --reload
# The command is: uvicorn <file_name>:<api_instance_name> --reload
# The file_name is the name of the file that contains the API code. In this case, it is app.py.
# The api_instance_name is the name of the API instance. In this case, it is api.
# The --reload parameter is used to reload the API when we make changes to the code. It is a good practice to use this parameter when we are developing the API.

# The syntax for the url is: http://<host>:<port>/<path_operation_decorator>/<path_operation_function>

# To see the automatic interactive API documentation by SwaggerUI, add /docs to the url.
# To see the ReDoc API documentation, add /redoc to the url.

