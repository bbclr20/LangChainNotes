# https://python.langchain.com/en/latest/modules/models/llms/examples/human_input_llm.html

# to simulate how a human would respond if they received the prompts
from langchain.llms.human import HumanInputLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

tools = load_tools(["wikipedia"])
llm = HumanInputLLM(
    prompt_func=lambda prompt: print(
        f"\n===PROMPT====\n{prompt}\n=====END OF PROMPT======"
    )
)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.run("What is 'Bocchi the Rock!'?")
