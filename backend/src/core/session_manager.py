from typing import Dict, Optional

# Global dictionary for in-memory session caching
PROCEEDING_CACHE: Dict[str, str] = {}


def save_session(session_id: str, text_content: str) -> None:
    """
    Save session content to the cache.
    
    Args:
        session_id: Unique identifier for the session
        text_content: Text content to cache
    """
    PROCEEDING_CACHE[session_id] = text_content


def get_session(session_id: str) -> Optional[str]:
    """
    Retrieve session content from the cache.
    
    Args:
        session_id: Unique identifier for the session
        
    Returns:
        The cached text content or None if not found
    """
    return PROCEEDING_CACHE.get(session_id)


def session_exists(session_id: str) -> bool:
    """
    Check if a session exists in the cache.
    
    Args:
        session_id: Unique identifier for the session
        
    Returns:
        True if the session exists, False otherwise
    """
    return session_id in PROCEEDING_CACHE