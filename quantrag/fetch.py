import json
import urllib.request
import urllib.parse
#fetch_summary is the fetch stage of the ingestion layer
#by pulling data from the API, i am able to parse this python dictionary and INSERT it into MariaDb to store it and have local cupy of the data 
from quantrag.config import USER_AGENT


#url-> request built from url-> response (send the request) -> raw_nytes -> dictionary 
def fetch_summary(tittle):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + tittle
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    response = urllib.request.urlopen(req)
    raw_bytes = response.read()
    return json.loads(raw_bytes) #jason turns the bytes into python dictionary


def fetch_article_text(title):
    parameters = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "titles": title,
        "format": "json",
        "formatversion": 2,
    }
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(parameters)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    data = json.loads(urllib.request.urlopen(req).read())
    page = data["query"]["pages"][0]
    return page["extract"]