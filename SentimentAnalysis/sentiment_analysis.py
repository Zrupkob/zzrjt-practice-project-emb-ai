# Import the requests library to handle HTTP requests
import requests, json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
     # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
    