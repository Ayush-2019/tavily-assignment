from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI


class CuratorAgent:
    def __init__(self):
        pass

    def curate_sources(self, query: str, sources: list):
        prompt = [{
            "role": "system",
            "content": "You are a tweet analyser. Your sole purpose is to choose 10 most relevant tweets for a given query.\n"
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Topic or Query: {query}\n"
                       f"Your sole purpose is to choose 10 most relevant tweets for a given query"
                       f"query\n "
                       f"Here is a list of articles:\n"
                       f"{sources}\n"
                       f"Please return nothing but a list of 10 json each having a tweet and the username who made the tweet in this structure: [json1,"
                       f"json2,json3,json4,json5,json6,json7,json8,json9,json10].\n "
        }]

        lc_messages = convert_openai_messages(prompt)
        response = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1).invoke(lc_messages).content
        chosen_sources = response
        print("curator response: ", chosen_sources)
        return chosen_sources

    def run(self, article: dict):
        article["sources"] = self.curate_sources(article["query"], article["sources"])
        return article
