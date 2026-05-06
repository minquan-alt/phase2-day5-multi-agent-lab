"""Benchmark skeleton for single-agent vs multi-agent."""

from time import perf_counter
from typing import Callable

from multi_agent_research_lab.core.schemas import BenchmarkMetrics
from multi_agent_research_lab.core.state import ResearchState


Runner = Callable[[str], ResearchState]


def run_benchmark(run_name: str, query: str, runner: Runner) -> tuple[ResearchState, BenchmarkMetrics]:
    """Measure latency and return a metric object."""

    started = perf_counter()
    state = runner(query)
    latency = perf_counter() - started
    
    # Calculate real cost and errors from state if available
    cost = getattr(state, "total_cost_usd", 0.0)
    quality = None # Peer review required, leaving as None instead of faking
    
    metrics = BenchmarkMetrics(
        run_name=run_name,
        latency_seconds=latency,
        quality_score=quality,
        estimated_cost_usd=cost
    )
    return state, metrics
