'''this code get sheet.csv and modify citation num and save in result.csv for OCL project'''

from scholarly import scholarly, ProxyGenerator
import pandas as pd
import requests

def schoolarCiteBy1(paper_name):
    '''return citation number  and use scholarly'''
    try:
        pg = ProxyGenerator()
        success = pg.ScraperAPI('8c96d0be287b8688b289902d909c30c0')
        scholarly.use_proxy(pg)
        search_query = scholarly.search_pubs(paper_name)
        paper = next(search_query)
        return paper['num_citations']
    except:
        return 0
    
def schoolarCiteBy2(query):
    '''return citation number  and use scholarly'''
    try:
        key = 'your_key'
        url = 'https://serpapi.com/search.json?engine=google_scholar&q=%s&api_key=%s' %(query , key)
        response = requests.get(url)
        return int(response.json()["organic_results"][0]["inline_links"]["cited_by"]["total"]) 
    except:
        return 0


def sheetAndReplace(path):
    df = pd.read_csv(path)
    for i in range(0 , len(df.index)):
       title = df.loc[i , 'Title']
       #citation = schoolarCiteBy1(title)
       citation = schoolarCiteBy2(title)
       print(citation)
       df.loc[i , 'Citation'] = citation    #modify dataframe
    df.to_csv('result.csv' , index=False)   #crate new result.csv with dataframe

path = "PATH"
sheetAndReplace(path)