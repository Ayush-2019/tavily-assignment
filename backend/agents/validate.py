from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI


class ValidateAgent:
    def __init__(self):
        pass

    def curate_sources(self, query):

        prompt = [{
            "role": "system",
            "content": "You are a personal health advisor. Your sole purpose is to choose 5 most relevant solution of a health problem including diet planning, exercise and other medical treatments "
                       "for me to read from a list of articles.\n "
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Topic or Query: {query}\n"
                       f"Your sole purpose is to determine whether the Topic or Query is a health problem\n."
                       f"Please return nothing but true if the Topic or Query is a health problem and False if it's not\n "
        }]

        lc_messages = convert_openai_messages(prompt)
        response = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1).invoke(lc_messages).content
        return response

    def run(self, article: dict):
        # print("query : ", article["query"])
        validity = self.curate_sources(article["query"])
        return validity
        # print("validity: " + validity)

