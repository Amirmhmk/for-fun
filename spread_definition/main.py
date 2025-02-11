import pandas as pd
import pprint
path = "D:/files/funnnnn/for-fun/spread_definition/definition"
with open(path, 'r') as file:
        text = file.read()

topic_defis = text.split("\n")
# print(topic_defis)
dec_topic_defi = {}
for i in topic_defis: 
        if i == "":
                continue
        
        topic_defi = i.split(":")
        dec_topic_defi[topic_defi[0]] = [topic_defi[1]]


df = pd.DataFrame(dec_topic_defi)
df = df.T

# Write the DataFrame to a CSV file
df.to_csv("test.csv", index=False)