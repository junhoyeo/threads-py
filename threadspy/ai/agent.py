import os
import sys
import logging
import itertools
from datetime import datetime
from langchain import PromptTemplate, LLMChain
from langchain.llms import LlamaCpp, OpenAIChat
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from ..threads_api import ThreadsAPI
from .templates import QA_template

# Set up logging
logging.basicConfig(filename='threads_agent.log', level=logging.INFO)

class ThreadsAgent:
    mode = None
    model = None
    mode_cpu = False
    mode_ppu = False
    mode_mps = False
    OPENAI_API_KEY = None
    threads_api = None

    def __init__(
        self,
        mode="openai",
        model=None,
        mode_cpu=True,
        mode_gpu=False,
        mode_mps=False,
        OPENAI_API_KEY=None,
        username=None,
        verbose=False,
    ):
        self.threads_api = ThreadsAPI(verbose=verbose, username=username)
        if mode in ["llama", "openai"]:
            if mode == "openai":
                try:
                    if OPENAI_API_KEY is not None:
                        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
                        self.OPENAI_API_KEY = OPENAI_API_KEY
                except:
                    logging.error("Please, export your OpenAI API KEY over 'OPENAI_API_KEY' environment variable")
                    logging.error("You may create the key here: https://platform.openai.com/account/api-keys")
                    sys.exit(1)
            if model is not None:
                self.model = model
            if mode is not None and mode in ["llama"]:
                if mode_mps:
                    self.mode_cpu = False
                    self.mode_gpu = False
                    self.mode_mps = True
                elif mode_gpu:
                    self.mode_cpu = False
                    self.mode_gpu = True
                    self.mode_mps = False
                elif mode_cpu:
                    self.mode_cpu = True
                    self.mode_gpu = False
                    self.mode_mps = False
            else:
                self.mode_cpu = False
                self.mode_gpu = False
                self.mode_mps = False
        else:
            raise "Choose a mode between 'llama' and 'openai'"

    def analysis_profile(
        self, username: str, boundary: str = "all", onlyText=False, sort="DESC"
    ):
        self.threads_api.username = username
        user_id = self.threads_api.get_user_id_from_username(username=username)
        if user_id is None:
            raise "[Auth] Private profiles cannot be analyzed."
        if boundary in ["all", "replies", "threads"]:
            threads = []
            if boundary in ["all", "replies"]:
                replies_tab = self.threads_api.get_user_profile_replies(
                    username=username, user_id=self.threads_api.user_id
                )
                threads.extend(replies_tab)
            if boundary in ["all", "threads"]:
                threads_tab = self.threads_api.get_user_profile_threads(
                    username=username, user_id=self.threads_api.user_id
                )
                threads.extend(threads_tab)
            threads = [
                [item["post"] for item in x.to_dict()["thread_items"]] for x in threads
            ]
            threads = list(itertools.chain(*threads))
            if sort == "DESC":
                threads.sort(key=lambda x: (x["taken_at"],))
            else:
                threads.sort(key=lambda x: (x["taken_at"] * -1,))
            threads = [
                {
                    "text": item["caption"]["text"],
                    "taken_at": str(datetime.fromtimestamp(item["taken_at"])),
                    "media": item["image_versions2"]["candidates"][0]
                    if len(item["image_versions2"]["candidates"]) > 0
                    else None,
                }
                if not onlyText
                else {
                    "text": item["caption"]["text"],
                    "taken_at": str(datetime.fromtimestamp(item["taken_at"])),
                }
                for item in threads
            ]
            # FIXME: connect llm
            return threads
        else:
            raise "[Error] Choose a boundary between 'all', 'replies' and 'threads'"

    def ask(self, question: str) -> str:
        """
        Returns answer

        Args:
            question (str): "What NFL team won the Super Bowl in the year Justin Bieber was born?"

        Returns:
            str: answer
        """
        template = QA_template
        prompt = PromptTemplate(template=template, input_variables=["question"])
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

        if self.mode == "llama":
            n_gpu_layers = 40
            if self.mode_mps:
                n_gpu_layers = 1
            n_batch = 128
            llm = LlamaCpp(
                model_path="./models/ggml-model-f16.bin",
                n_gpu_layers=n_gpu_layers,
                n_batch=n_batch,
                f16_kv=self.mode_mps,
                callback_manager=callback_manager,
                verbose=True,
            )
        elif self.mode == "openai":
            if self.model == None:
                model = "gpt3.5-turbo"
            llm = OpenAIChat(
                model=model,
                callback_manager=callback_manager,
            )
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        answer = llm_chain.run(question)

        # Log the question and answer
        logging.info(f"Question: {question}")
        logging.info(f"Answer: {answer}")

        return answer
