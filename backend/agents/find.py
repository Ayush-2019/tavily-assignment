from tavily import TavilyClient
import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


class FindAgent:
    def __init__(self):
        pass

    def search_tavily(self, query: str):
        results = tavily_client.search(query=query, topic="news", max_results=10)
        sources = results["results"]
        return sources

    def run(self, article: dict):
        res = self.search_tavily(article["query"])
        article["sources"] = res[0]
        return article
