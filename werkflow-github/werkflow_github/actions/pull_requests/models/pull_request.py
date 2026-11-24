from typing import Any, Dict

from .pull_request_ref import PullRequestRef
from .pull_request_validator import PullRequestValidator


class PullRequest:

    def __init__(self, data: Dict[str, Any]) -> None:
        payload = dict(data)

        head = payload.get('head')
        if isinstance(head, dict):
            payload['head'] = PullRequestRef(head)

        base = payload.get('base')
        if isinstance(base, dict):
            payload['base'] = PullRequestRef(base)

        self.data = PullRequestValidator(**payload)
