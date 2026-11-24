import datetime
from typing import Any, Dict, List, Optional

from werkflow_github.actions.common.models import (
    Conclusion,
    ConclusionMap,
    Status,
    StatusMap,
)
from werkflow_github.actions.pull_requests.models import PullRequest

from .workflow_validator import WorkflowValidator


def _parse_timestamp(value: Any) -> Optional[datetime.datetime]:
    if value is None:
        return None
    if isinstance(value, datetime.datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))
    return None


class Workflow:

    def __init__(self, data: Dict[str, Any]) -> None:
        self._status_map = StatusMap()
        self._conclusion_map = ConclusionMap()

        payload = dict(data)

        raw_pull_requests: List[Any] = payload.pop('pull_requests', None) or []
        parsed_pull_requests = [
            pr if isinstance(pr, PullRequest) else PullRequest(pr)
            for pr in raw_pull_requests
        ]

        raw_conclusion = payload.pop('conclusion', None)
        if isinstance(raw_conclusion, Conclusion):
            parsed_conclusion: Optional[Conclusion] = raw_conclusion
        else:
            parsed_conclusion = self._conclusion_map.get(raw_conclusion)

        raw_status = payload.pop('status', None)
        if isinstance(raw_status, Status):
            parsed_status: Status = raw_status
        else:
            parsed_status = self._status_map.get(raw_status) or Status.QUEUED

        created_at = _parse_timestamp(payload.pop('created_at', None))
        updated_at = _parse_timestamp(payload.pop('updated_at', None))
        run_started_at = _parse_timestamp(payload.pop('run_started_at', None))

        if created_at is not None:
            payload['created_at'] = created_at
        if updated_at is not None:
            payload['updated_at'] = updated_at
        if run_started_at is not None:
            payload['run_started_at'] = run_started_at

        self.data = WorkflowValidator(
            **payload,
            conclusion=parsed_conclusion,
            status=parsed_status,
            pull_requests=parsed_pull_requests,
        )

    @property
    def state(self) -> Status:
        return self.data.status

    @property
    def status(self) -> Optional[Conclusion]:
        return self.data.conclusion
