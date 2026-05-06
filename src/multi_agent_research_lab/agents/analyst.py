"""Analyst agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class AnalystAgent(BaseAgent):
    """Turns research notes into structured insights."""

    name = "analyst"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.analysis_notes`."""
        from multi_agent_research_lab.services.llm_client import LLMClient
        llm_client = LLMClient()
        
        system_prompt = "You are an analyst extracting key claims."
        user_prompt = f"Analyze these notes: {state.research_notes}"
        response = llm_client.complete(system_prompt, user_prompt)
        
        state.analysis_notes = response.content
        state.total_cost_usd += response.cost_usd or 0.0
        return state
