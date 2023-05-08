# https://python.langchain.com/en/latest/modules/prompts/prompt_templates/getting_started.html
from langchain import PromptTemplate
from langchain.prompts import load_prompt
from langchain import PromptTemplate

#
# Create a prompt template
#

# An example prompt with multiple input variables
multiple_input_prompt = PromptTemplate(
    input_variables=["adjective", "content"],
    template="Tell me a {adjective} joke about {content}.",
)
print(
    multiple_input_prompt.format(adjective="funny", content="chickens")
)  # -> "Tell me a funny joke about chickens."

# An example of from_template
template = "Tell me a {adjective} joke about {content}."
prompt_template = PromptTemplate.from_template(template)
print(prompt_template.input_variables)  # -> ['adjective', 'content']
print(
    prompt_template.format(adjective="funny", content="chickens")
)  # -> Tell me a funny joke about chickens.

#
# Serialize prompt template
#
prompt_template.save("awesome_prompt.json")
loaded_prompt = load_prompt("awesome_prompt.json")
assert prompt_template == loaded_prompt
