# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:41:21 2023

@author: jeongseungeun
"""

def crawling():

    from tqdm import tqdm
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import time
    
    n = int(input("크롤링 할 페이지 수를 적어주세요: "))
    
    reviews = []
    review_data=[]
    
    for page in tqdm(range(1,n+1)):
        url = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
        html = requests.get(url)
        soup = BeautifulSoup(html.content,'html.parser')
        reviews = soup.find_all("td",{"class":"title"})
    
        for review in reviews:
            sentence = review.find("a",{"class":"report"}).get("onclick").split("', '")[2]
            if sentence != "":
                score = review.find("em").get_text()
                review_data.append([sentence,int(score)])
    time.sleep(0.1)
     
    df = pd.DataFrame(review_data, columns=['sentence','score'])
    df.to_csv("crawling_data.csv", encoding ="utf-8", index=False)
