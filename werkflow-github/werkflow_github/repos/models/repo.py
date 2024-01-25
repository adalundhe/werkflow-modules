from typing import Dict, Any
from .repo_validator import RepoValidator


class Repo:

    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = RepoValidator(
            **data
        )