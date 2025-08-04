class ProceedingNotFoundError(Exception):
    """Exception raised when a proceeding is not found."""
    
    def __init__(self, message: str = "Proceeding not found") -> None:
        """
        Initialize the exception.
        
        Args:
            message: Explanation of the error
        """
        self.message = message
        super().__init__(self.message)