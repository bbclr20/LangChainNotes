# https://python.langchain.com/en/latest/modules/models/llms/getting_started.html
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

# # passing in a string and getting back a string
# res = llm("Tell me a joke")
# print(res)

# More broadly, you can call it with a list of inputs,
# getting back a more complete response than just the text.
input_strings = ["Tell me a joke", "Tell me a poem"]
llm_result = llm.generate(input_strings)

for input_string, res in zip(input_strings, llm_result.generations):
    print(input_string)
    print(res)
