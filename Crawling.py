from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import pandas as pd

reviews = []
review_data=[]

for page in tqdm(range(1,2)):
    url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
    html = requests.get(url)
    soup = BeautifulSoup(html.content,'html.parser')
    reviews = soup.find_all("td",{"class":"title"})
    
    for review in reviews:
        sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
        if sentence != "":
            score = review.find("em").get_text()
            review_data.append([sentence,int(score)])
     
df = pd.DataFrame(review_data, columns=['sentence','score'])

df.to_csv("sample.csv", encoding='utf-8', index=False)