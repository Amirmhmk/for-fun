import openai
import json

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def save_prompt_and_response(prompt, response, filename="gpt_responses.json"):
    try:
        with open(filename, 'a') as f:
            data = {
                "prompt": prompt,
                "response": response
            }
            f.write(json.dumps(data) + "\n")
        print(f"Prompt and response saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    prompt = "hi \n introduce yourself."
    response = get_gpt_response(prompt)
    print(f"GPT-3 Response: {response}")
    # save_prompt_and_response(prompt, response)

if __name__ == "__main__":
    main()
