import openai
from openai import OpenAIError  

def getContent():
    with open ("recipe.txt", 'r+') as file:
        fileData =file.readline().strip()
    values = [value.strip() for value in fileData.split(',')]
    content = None
    if len(values) ==4:
        runFlag, cuisine, course, flavor = values
        if runFlag == 'run':
            content = "Give me a recipe for " + cuisine + " cusine that is a " + course +" and is " +flavor+"."
    return content

        
def writeContent(response):
    with open("recipe.txt", 'w+') as file:
        file.write(response)

def getAPIKey():
    with open("apiKey.txt", 'r') as file:
        key = file.readline().strip()
    return key

def main():
    content = getContent()
    if content is not None:
        client = openai.Client(
            base_url="https://openrouter.ai/api/v1",
            api_key=getAPIKey())  

        messages1 = [{"role": "user", "content": content }]

        try:
            completion = client.chat.completions.create(
                model="google/gemini-flash-1.5-8b-exp",
                messages=messages1
            )

            response = (completion.choices[0].message.content)
            writeContent(response)
            

        except openai.APIError as e:
            # Handle quota error
            if e.code == "insufficient_quota":
                print("Error: You have exceeded your quota. Please check your OpenAI account and purchase more credits.")
            else:
                print(f"OpenAI API Error: {e}")

        except OpenAIError as e:
            print(f"OpenAI Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")



while True:
    main()