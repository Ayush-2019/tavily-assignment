from langgraph.graph import Graph
from .agents import FindAgent, ConsolidateAgent, WriterAgent


class MasterAgent:

    def run(self, query):
        search_agent = FindAgent()
        curator_agent = ConsolidateAgent()
        writer_agent = WriterAgent()

        workflow = Graph()

        workflow.add_node("search", search_agent.run)
        workflow.add_node("curate", curator_agent.run)
        workflow.add_node("write", writer_agent.run)

        workflow.add_edge('search', 'curate')
        workflow.add_edge('curate', 'write')

        workflow.set_entry_point("search")
        workflow.set_finish_point("write")

        chain = workflow.compile()

        results = chain.invoke({"query": query})

        return results
