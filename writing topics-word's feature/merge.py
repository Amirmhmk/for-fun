import pandas as pd
import pprint

def sheetAndReplace(path):
    df = pd.read_csv(path , header = None)

    num_of_rows , num_of_columns = df.shape

    topic_words = {}
    for i in range (0 , num_of_columns):
        topic = df.loc[0 , i]
        topic_words[topic] =[]
        for j in range(1 , num_of_rows):
            feature = df.loc[ j , i]
            if pd.isna(feature):
                break
            topic_words[topic].append(feature)
        
    with open("Topic_word_features.txt"  , 'w') as file:
        for topic in topic_words:
            file.write(topic + ' : ')
            for feature in topic_words[topic]:
                file.write(feature + " , ")
            file.write("\n\n")
        

path = "PATH"
sheetAndReplace(path)