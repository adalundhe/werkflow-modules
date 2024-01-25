from typing import Dict, Any
from .repo_ref_validator import RepoRefValidator


class RepoRef:

    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = RepoRefValidator(
            **data
        )