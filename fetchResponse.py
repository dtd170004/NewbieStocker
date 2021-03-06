import requests


def fetchStockData(ticker, API_key):
    
    #Prep parameters to pass to server
    financial_API_URL = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
    financial_API_query = {"symbol": ticker}
    financial_API_headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': API_key,
        "Content-Type": "application/json"
    }
    
    #Request from RapidAPI server
    #Query Yahoo-finance.
    response = requests.request("GET", financial_API_URL,
                            headers= financial_API_headers,
                            params= financial_API_query)
    
    if(response.status_code == 200):
        #Return content of response
        return response.text
    else:
        #Return error code from server
        return "Failed to communicate with X-RapidAPI. Status response: " + str(response.status_code)