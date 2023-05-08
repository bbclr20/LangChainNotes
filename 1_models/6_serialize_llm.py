# https://python.langchain.com/en/latest/modules/models/llms/examples/llm_serialization.html
from langchain.llms.loading import load_llm

llm = load_llm("llm.json")
res = llm("Tell me a joke")
print(res)
# llm.save("llm.json")
