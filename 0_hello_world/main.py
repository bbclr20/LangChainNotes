# export the env or set the env here
# import os
# os.environ["OPENAI_API_KEY"] = "<your key>"

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)
res = chain.run("colorful socks")
print(res)
