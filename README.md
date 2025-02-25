# CS361-Microservice_A

This is the microservice A that I have implemented for my partner.  
This is an artifical intelligence powered recipe generator that relies on the user writing a list of parameters (cusineType, dishType, and tasteDescriptor) to the recipe.txt file in the following format:

![image](https://github.com/user-attachments/assets/c83e743b-bcda-4b2e-85de-599005d496d9)

The 'run' should be in all lowercase and is required as the first paramater so the microservice knows to start the program.

The microservice will then read this recipe.txt file and extract the data, using it to generate a call to a Large Language Model (LLM). In this case, the model used is an experimental verison of Gemini.
The microservice will then get a recipe from this LLM that fits the parameters before writing it back to the recipe.txt file. The recipe will look something like this:

![image](https://github.com/user-attachments/assets/a0577f95-6ceb-4ec3-96df-388399020bb1)

To adapt this program for your personal use you will need to create a new api key that will link to the large language model.
To do this, create a file called "apiKey.txt." In this file, you will need to put a personalized api key that can be created at the following link: https://openrouter.ai/


UML Diagram:
![Blank diagram](https://github.com/user-attachments/assets/f10fb443-dfcb-4597-93fe-fdc8d5c112ff)
