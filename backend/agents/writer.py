from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI
import json5 as json

sample_json = """
{
  "username": Username of the person who wrote the tweet,
  "tweet": "tweet content"
}
"""


class WriterAgent:
    def __init__(self):
        pass

    def writer(self, query: str, sources: list):

        prompt = [{
            "role": "system",
            "content": "You are an tweet writer. Your sole purpose is to write the tweet about a  "
                       "topic\n "
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Query or Topic: {query}"

                       
                       f"Source: {sources}\n"
                       f"Your sole purpose is to choose 10 most relevant tweets for a given query"
                       f"topic based on the sources.\n "
                       f"Please return nothing but an array of 5 JSON objects in the following format:\n"
                       f"{sample_json}\n "

        }]

        lc_messages = convert_openai_messages(prompt)
        optional_params = {
            "response_format": {"type": "json_object"}
        }

        response = ChatOpenAI(model='gpt-4-0125-preview', max_retries=1, model_kwargs=optional_params).invoke(lc_messages).content
        # print("writer response: ", re)
        return json.loads(response)

    def run(self, article: dict):
        article.update(self.writer(article["query"], article["sources"]))
        return article
