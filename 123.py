import requests
from bs4 import BeautifulSoup
 
url = "https://www.bbc.com/news"
 
response = requests.get(url)
 
if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, "html.parser")
 
    headlines = soup.find_all("h2")
 
    for headline in headlines:
        print(headline.text.strip())
 
else:
    print("Error!  ", response.status_code)