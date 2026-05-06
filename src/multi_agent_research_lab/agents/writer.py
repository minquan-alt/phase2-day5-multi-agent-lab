"""Writer agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class WriterAgent(BaseAgent):
    """Produces final answer from research and analysis notes."""

    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.final_answer`."""
        from multi_agent_research_lab.services.llm_client import LLMClient
        llm_client = LLMClient()
        
        system_prompt = "You are a writer creating the final answer."
        user_prompt = f"Write final answer from: {state.analysis_notes}"
        response = llm_client.complete(system_prompt, user_prompt)
        
        state.final_answer = response.content
        state.total_cost_usd += response.cost_usd or 0.0
        return state
