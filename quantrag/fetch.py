import json
import urllib.request
#this is going to be my data ingestion layer function 
#by pulling data from the API, i am able to parse this python dictionary and INSERT it into MariaDb to store it and have local cupy of the data 
from quantrag.config import USER_AGENT

#url-> request built from url-> response (send the request) -> raw_nytes -> dictionary 
def fetch_summary(tittle):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + tittle
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    response = urllib.request.urlopen(req)
    raw_bytes = response.read()
    return json.loads(raw_bytes) #jason turns the bytes into python dictionary