import pandas as pd
import google.generativeai as genai
import time
import os

# Configure Gemini API
API_KEY = "AIzaSyDQZtt7GtXRuSOpYESOtfNXLm_lsOHjgbc"
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash-exp')  # Choose the appropriate model  gemini-1.5-flash

# Prompt to attach to each abstract
PROMPT = """I am working on a scientific subject and I need to categorize some article to three categories(low , medium and high)based on their abstract. I will send abstract of one of them and definition of categories then send its category without and reasoning. just say high , low or medium.

Low Relevance: Publications that apply artificial intelligence (AI) and machine learning (ML) techniques to network security, including anomaly detection and classification methods, but without any focus on continual learning paradigms. These studies typically use static or batch learning approaches and do not address challenges like evolving data distributions or knowledge retention.

Medium Relevance: Publications that incorporate lifelong learning or data stream-based learning methodologies (such as incremental learning) within network security applications. These works explore adaptive models that can handle non-stationary data but may lack a comprehensive framework for continual learning or only partially address issues like catastrophic forgetting.

High Relevance: Publications that explicitly investigate continual learning approaches in network security, focusing on mechanisms to mitigate catastrophic forgetting, improve model adaptation over time, and enhance robustness against evolving cyber threats. These studies often implement strategies like experience replay, regularization-based techniques, or dynamic architectures but may not be fully optimized for real-time learning.

Very High Relevance: Publications that develop and implement online continual learning frameworks in network security. These studies emphasize real-time adaptation, learning from continuous and evolving data streams, and effectively addressing challenges like concept drift, catastrophic forgetting, and knowledge transfer in a dynamic threat landscape. They align closely with our projects objectives by enabling security models to continuously evolve with minimal human intervention.

Abstract: 
"""

# Input and output file paths
INPUT_CSV = "IN3.csv" # "input_abstracts.csv"
OUTPUT_CSV = "output_responses.csv"

# Function to send request to Gemini API
def send_to_gemini(abstract):
    try:
        full_prompt = PROMPT + abstract  # Attach the prompt
        response = model.generate_content(full_prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Read abstracts from input CSV
df = pd.read_csv(INPUT_CSV)

# Check if output file exists to determine whether to write header
file_exists = os.path.isfile(OUTPUT_CSV)

# Open the output file in append mode
with open(OUTPUT_CSV, mode='a', encoding='utf-8', newline='') as f:
    # Process each abstract one by one
    for index, row in df.iterrows():
        abstract = row["Abstract"]
        print(f"Processing abstract {index + 1}...")

        # Send the abstract to Gemini API
        response = send_to_gemini(abstract)
        print(f"Response received: {response[:50]}...")  # Print first 50 chars

        # Save incrementally
        output_df = pd.DataFrame([[abstract, response]], columns=["Abstract", "Response"])
        output_df.to_csv(f, header=not file_exists, index=False)
        file_exists = True  # Ensure header is written only once

        # Wait before sending the next request
        time.sleep(10)

print(f"Responses saved incrementally to {OUTPUT_CSV}")









####################################################################################

# import pandas as pd
# import google.generativeai as genai
# import time

# # Configure Gemini API
# API_KEY = "AIzaSyDQZtt7GtXRuSOpYESOtfNXLm_lsOHjgbc"
# genai.configure(api_key=API_KEY)

# # Initialize the Gemini model
# model = genai.GenerativeModel('gemini-1.5-flash')  # Use the appropriate model  name   gemini-1.5-flash   gemini-pro
   
# # Prompt to attach to each abstract
# PROMPT = """I am working on a scientific subject and I need to categorize some article to three categories(low , medium and high)based on their abstract. I will send abstract of one of them and definition of categories then send its category without and reasoning. just say high , low or medium.

# Low Relevance: Publications that apply artificial intelligence (AI) and machine learning (ML) techniques to network security, including anomaly detection and classification methods, but without any focus on continual learning paradigms. These studies typically use static or batch learning approaches and do not address challenges like evolving data distributions or knowledge retention.

# Medium Relevance: Publications that incorporate lifelong learning or data stream-based learning methodologies (such as incremental learning) within network security applications. These works explore adaptive models that can handle non-stationary data but may lack a comprehensive framework for continual learning or only partially address issues like catastrophic forgetting.

# High Relevance: Publications that explicitly investigate continual learning approaches in network security, focusing on mechanisms to mitigate catastrophic forgetting, improve model adaptation over time, and enhance robustness against evolving cyber threats. These studies often implement strategies like experience replay, regularization-based techniques, or dynamic architectures but may not be fully optimized for real-time learning.

# Very High Relevance: Publications that develop and implement online continual learning frameworks in network security. These studies emphasize real-time adaptation, learning from continuous and evolving data streams, and effectively addressing challenges like concept drift, catastrophic forgetting, and knowledge transfer in a dynamic threat landscape. They align closely with our projects objectives by enabling security models to continuously evolve with minimal human intervention.

# Abstract: 
# """

# # Input and output file paths
# INPUT_CSV = "input_abstracts.csv"
# OUTPUT_CSV = "output_responses.csv"

# # Function to send request to Gemini API
# def send_to_gemini(abstract):
#     try:
#         # Attach the prompt to the abstract
#         full_prompt = PROMPT + abstract
        
#         # Send the request to the Gemini API
#         response = model.generate_content(full_prompt)
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Read abstracts from the input CSV
# df = pd.read_csv(INPUT_CSV)

# # Ensure the output DataFrame has a column for responses
# df["response"] = ""

# # Process each abstract one by one
# for index, row in df.iterrows():
#     abstract = row["Abstract"]
#     print(abstract)
#     try:
#         # Send the abstract to the Gemini API
#         response = send_to_gemini(abstract)
#         df.at[index, "response"] = response
#         print(f"Processed abstract {index + 1}: {response}...")  # Print first 50 chars of response
#     except Exception as e:
#         df.at[index, "response"] = f"Error: {str(e)}"
#         print(f"Failed to process abstract {index + 1}: {str(e)}")
    
#     # Wait for 1 second before sending the next request
#     time.sleep(10)

# # Save the responses to a new CSV file
# df.to_csv(OUTPUT_CSV, index=False)
# print(f"Responses saved to {OUTPUT_CSV}")







# import google.generativeai as genai


# prompt = """
# I am working on a scientific subject and I need to categorize some article to three categories(low , medium and high)based on their abstract. I will send abstract of one of them and definition of categories then send its category without and reasoning. just say high , low or medium.



# Low Relevance: Publications that apply artificial intelligence (AI) and machine learning (ML) techniques to network security, including anomaly detection and classification methods, but without any focus on continual learning paradigms. These studies typically use static or batch learning approaches and do not address challenges like evolving data distributions or knowledge retention.

# Medium Relevance: Publications that incorporate lifelong learning or data stream-based learning methodologies (such as incremental learning) within network security applications. These works explore adaptive models that can handle non-stationary data but may lack a comprehensive framework for continual learning or only partially address issues like catastrophic forgetting.



# High Relevance: Publications that explicitly investigate continual learning approaches in network security, focusing on mechanisms to mitigate catastrophic forgetting, improve model adaptation over time, and enhance robustness against evolving cyber threats. These studies often implement strategies like experience replay, regularization-based techniques, or dynamic architectures but may not be fully optimized for real-time learning.



# Very High Relevance: Publications that develop and implement online continual learning frameworks in network security. These studies emphasize real-time adaptation, learning from continuous and evolving data streams, and effectively addressing challenges like concept drift, catastrophic forgetting, and knowledge transfer in a dynamic threat landscape. They align closely with our projects objectives by enabling security models to continuously evolve with minimal human intervention.



# abstract: """

# abstarct = """Deep Learning based Intrusion Detection Systems (IDSs) have received significant attention from the research community for their capability to handle modern-day security systems in large-scale networks. Despite their considerable improvement in performance over machine learning-based techniques and conventional statistical models, deep neural networks (DNN) suffer from catastrophic forgetting: the model forgets previously learned information when trained on newer data points. This vulnerability is specifically exaggerated in large scale systems due to the frequent changes in network architecture and behaviours, which leads to changes in data distribution and the introduction of zero-day attacks; this phenomenon is termed as covariate shift. Due to these constant changes in the data distribution, the DNN models will not be able to consistently perform at high accuracy and low false positive rate (FPR) rates without regular updates. However, before we update the DNN models, it is essential to understand the magnitude and nature of the drift in the data distribution. In this paper, to analyze the drift in data distribution, we propose an eight-stage statistics and machine learning guided implementation framework that objectively studies and quantifies the changes. Further, to handle the changes in data distribution, most IDS solutions collect the network packets and store them to retrain the DNN models periodically, but when the network’s size and complexity increase, those tasks become expensive. To efficiently solve this problem, we explore the potential of continual learning models to incrementally learn new data patterns while also retaining their previous knowledge. We perform an experimental and analytical study of advanced intrusion detection systems using three major continual learning approaches: learning without forgetting, experience replay, and dark experience replay on the NSL-KDD and the CICIDS 2017 dataset. Through extensive experimentation, we show that our continual learning models achieve improved accuracy and lower FPR rates when compared to the state-of-the-art works while also being able to incrementally learn newer data patterns. Finally, we highlight the drawbacks of traditional statistical and non-gradient based machine learning approaches in handling the covariate shift problem."""
# genai.configure(api_key="AIzaSyDQZtt7GtXRuSOpYESOtfNXLm_lsOHjgbc")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(prompt + abstarct)
# print(response.text)




















# import requests
# import csv

# # Replace with your Gemini API endpoint and API key
# API_URL = "https://api.gemini.com/v1/your-endpoint"
# API_KEY = "your-api-key"

# # The sentence you want to send to the Gemini API
# sentence = "Hello, how are you?"

# # Headers for the API request
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# # Payload to send to the API
# payload = {
#     "sentence": sentence
# }

# # Send the request to the Gemini API
# response = requests.post(API_URL, headers=headers, json=payload)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the response JSON
#     response_data = response.json()
    
#     # Extract the answer from the response (adjust based on the API's response structure)
#     answer = response_data.get("answer", "No answer found")
    
#     # Write the sentence and answer to a CSV file
#     with open("gemini_response.csv", mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Sentence", "Answer"])  # Write header
#         writer.writerow([sentence, answer])      # Write data
    
#     print("Response written to gemini_response.csv")
# else:
#     print(f"Failed to get a response. Status code: {response.status_code}")
#     print(response.text)