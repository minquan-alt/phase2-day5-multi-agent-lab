"""Supervisor / router skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.state import ResearchState


class SupervisorAgent(BaseAgent):
    """Decides which worker should run next and when to stop."""

    name = "supervisor"

    def run(self, state: ResearchState) -> ResearchState:
        """Update `state.route_history` with the next route."""
        if state.iteration >= 5:
            state.record_route("done")
            return state

        if not state.route_history:
            state.record_route("researcher")
        elif state.route_history[-1] == "researcher":
            state.record_route("analyst")
        elif state.route_history[-1] == "analyst":
            state.record_route("writer")
        else:
            state.record_route("done")
            
        return state
