"""Search client abstraction for ResearcherAgent."""

from multi_agent_research_lab.core.errors import StudentTodoError
from multi_agent_research_lab.core.schemas import SourceDocument


class SearchClient:
    """Provider-agnostic search client skeleton."""

    def search(self, query: str, max_results: int = 5) -> list[SourceDocument]:
        """Search for documents relevant to a query."""
        # Local mock implementation
        return [
            SourceDocument(
                url=f"https://mock.example.com/{i}",
                title=f"Mock Result {i} for {query[:10]}",
                snippet=f"This is a mock snippet for result {i} containing information about {query}."
            )
            for i in range(max_results)
        ]
