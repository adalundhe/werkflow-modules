from typing import Any, Dict

from werkflow_github.repos.models import RepoRef

from .pull_request_ref_validator import PullRequestRefValidator


class PullRequestRef:

    def __init__(self, data: Dict[str, Any]) -> None:
        payload = dict(data)

        repo = payload.get('repo')
        if isinstance(repo, dict):
            payload['repo'] = RepoRef(repo)

        self.data = PullRequestRefValidator(**payload)
