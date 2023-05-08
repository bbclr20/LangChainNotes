# https://python.langchain.com/en/latest/modules/models/llms/examples/custom_llm.html
from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class CustomLLM(LLM):
    n: int

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        """A _call method that takes in a string,
        some optional stop words, and returns a string
        """
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[: self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """An _identifying_params property that is used to help
        with printing of this class. Should return a dictionary
        """
        return {"n": self.n}


if __name__ == "__main__":
    llm = CustomLLM(n=10)
    res = llm("This is a foobar thing")
    print(f"res: {res}")
    print(llm)
