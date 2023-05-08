# https://python.langchain.com/en/latest/modules/models/llms/examples/llm_caching.html
from langchain.llms import OpenAI
import langchain
from langchain.cache import InMemoryCache
from time import time

langchain.llm_cache = InMemoryCache()
# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

# ask and cache the result
s = time()
res = llm("Tell me a joke")
print(res)
escape = time() - s
print(f"escape: {escape:.3}s")

# use the cache result
s = time()
res = llm("Tell me a joke")
print(res)
escape = (time() - s) * 1000
print(f"escape: {escape:.3}ms")
