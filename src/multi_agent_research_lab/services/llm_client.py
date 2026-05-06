"""LLM client abstraction.

Production note: agents should depend on this interface instead of importing an SDK directly.
"""

from dataclasses import dataclass

from multi_agent_research_lab.core.errors import StudentTodoError


@dataclass(frozen=True)
class LLMResponse:
    content: str
    input_tokens: int | None = None
    output_tokens: int | None = None
    cost_usd: float | None = None


class LLMClient:
    """Provider-agnostic LLM client skeleton."""

    def complete(self, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Return a model completion."""
        import os
        import google.generativeai as genai
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return LLMResponse(
                content=f"Mock LLM response for: {user_prompt[:50]}...",
                input_tokens=10,
                output_tokens=20,
                cost_usd=0.001
            )
            
        try:
            genai.configure(api_key=api_key)
            model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=system_prompt
            )
            response = model.generate_content(user_prompt)
            content = response.text
            
            in_tokens = 0
            out_tokens = 0
            if hasattr(response, 'usage_metadata'):
                in_tokens = response.usage_metadata.prompt_token_count
                out_tokens = response.usage_metadata.candidates_token_count
                
            cost_usd = (in_tokens * 0.075 + out_tokens * 0.30) / 1000000
            return LLMResponse(
                content=content,
                input_tokens=in_tokens,
                output_tokens=out_tokens,
                cost_usd=cost_usd
            )
        except Exception as e:
            return LLMResponse(
                content=f"Error calling LLM: {str(e)}",
                input_tokens=0,
                output_tokens=0,
                cost_usd=0.0
            )
