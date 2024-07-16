import os
import time
from concurrent.futures import ThreadPoolExecutor
from langgraph.graph import Graph

# Import agent classes
from .agents import ValidateAgent


class MasterAgent:

    def run(self, query):
        # Initialize agents
        validate_agent = ValidateAgent()
        # search_agent = SearchAgent()
        # curator_agent = CuratorAgent()
        # writer_agent = WriterAgent()
        # critique_agent = CritiqueAgent()
        # designer_agent = DesignerAgent(self.output_dir)
        # # editor_agent = EditorAgent(layout)
        # publisher_agent = PublisherAgent(self.output_dir)

        # Define a Langchain graph
        workflow = Graph()

        # Add nodes for each agent
        workflow.add_node("validate", validate_agent.run)
        # workflow.add_node("search", search_agent.run)
        # workflow.add_node("curate", curator_agent.run)
        # workflow.add_node("write", writer_agent.run)
        # workflow.add_node("critique", critique_agent.run)
        # workflow.add_node("design", designer_agent.run)

        # # Set up edges
        # workflow.add_edge('search', 'curate')
        # workflow.add_edge('curate', 'write')
        # workflow.add_edge('write', 'critique')
        # workflow.add_conditional_edges(start_key='critique',
        #                                condition=lambda x: "accept" if x['critique'] is None else "revise",
        #                                conditional_edge_mapping={"accept": "design", "revise": "write"})

        # set up start and end nodes
        workflow.set_entry_point("validate")
        workflow.set_finish_point("validate")

        # compile the graph
        chain = workflow.compile()


        result = validate_agent.run(query)

        return result
    
