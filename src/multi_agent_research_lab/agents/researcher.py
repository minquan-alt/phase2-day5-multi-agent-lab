"""Researcher agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class ResearcherAgent(BaseAgent):
    """Collects sources and creates concise research notes."""

    name = "researcher"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.sources` and `state.research_notes`."""
        from multi_agent_research_lab.services.search_client import SearchClient
        from multi_agent_research_lab.services.llm_client import LLMClient
        
        search_client = SearchClient()
        llm_client = LLMClient()
        
        sources = search_client.search(state.request.query)
        state.sources.extend(sources)
        
        system_prompt = "You are a researcher summarizing findings."
        user_prompt = f"Summarize findings for: {state.request.query}"
        response = llm_client.complete(system_prompt, user_prompt)
        
        state.research_notes = response.content
        state.total_cost_usd += response.cost_usd or 0.0
        return state
