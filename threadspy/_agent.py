from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class ThreadsAgent:
    mode = "cpu"

    def __init__(self, mode="cpu"):
        self.mode = mode

    def ask(self, question: str):
        """
        Returns answer

        Args:
            question (str): "What NFL team won the Super Bowl in the year Justin Bieber was born?"

        Returns:
            str: answer
        """
        template = """Question: {question}
        Answer: Let's work this out in a step by step way to be sure we have the right answer."""
        prompt = PromptTemplate(template=template, input_variables=["question"])

        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

        n_gpu_layers = 40
        if self.mode == "metal":
            n_gpu_layers = 1
        n_batch = 512

        llm = LlamaCpp(
            model_path="./models/ggml-model-f16.bin",
            n_gpu_layers=n_gpu_layers,
            n_batch=n_batch,
            f16_kv=(self.mode == "metal"),
            callback_manager=callback_manager,
            verbose=True,
        )
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        return llm_chain.run(question)
