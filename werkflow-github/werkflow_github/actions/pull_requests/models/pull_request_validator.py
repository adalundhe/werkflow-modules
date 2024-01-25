from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    AnyHttpUrl
)
from typing import List, Any, Dict


class PullRequestRepoValidator(BaseModel):
    id: StrictInt
    url: AnyHttpUrl
    name: StrictStr


class PullRequestRepo:

    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = PullRequestRepoValidator(
            **data
        )


class PullRequestRefValidator(BaseModel):
    ref: StrictStr
    sha: StrictStr
    repo: PullRequestRepo


class PullRequestRef:
    
    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = PullRequestRefValidator(
            **data
        )


class PullRequestValidator(BaseModel):
    id: StrictInt
    number: StrictInt
    url: AnyHttpUrl
    head: PullRequestRef
    base: PullRequestRef


class PullRequest:

    def __init__(
        self,
        data: Dict[str, Any]
    ) -> None:
        self.data = PullRequestValidator(
            **data
        )