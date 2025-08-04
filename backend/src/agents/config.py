from typing import Dict, Any

# Global dictionary containing agent configurations
AGENTS: Dict[str, Dict[str, Any]] = {
    "summary_agent": {
        "name": "Summary Agent",
        "description": "Agent responsible for summarizing legal proceedings and documents",
        "llm_model": "gemini-pro",
        "system_prompt": "You are a legal expert specialized in summarizing court proceedings and legal documents. Provide concise, accurate summaries that capture the key points, decisions, and implications of legal matters."
    },
    "chat_agent": {
        "name": "Chat Agent",
        "description": "Agent for interactive legal consultation and question answering",
        "llm_model": "gemini-pro",
        "system_prompt": "You are a legal assistant helping lawyers and legal professionals with their queries. Provide accurate, well-reasoned responses based on legal principles and precedents. Be concise but thorough in your explanations."
    }
}