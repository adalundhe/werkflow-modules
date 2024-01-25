from typing import Dict, Any
from .pull_request_ref_validator import PullRequestRefValidator

class PullRequestRef:
    
    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = PullRequestRefValidator(
            **data
        )