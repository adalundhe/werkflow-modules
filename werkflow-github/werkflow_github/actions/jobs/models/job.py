import datetime
import re
from typing import Any, Dict, List, Optional

from werkflow_github.actions.common.models import (
    Conclusion,
    ConclusionMap,
    Status,
    StatusMap,
)
from werkflow_github.actions.steps.models import Step

from .job_validator import JobValidator


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


class Job:

    def __init__(self, data: Dict[str, Any]) -> None:
        self._status_map = StatusMap()
        self._conclusion_map = ConclusionMap()

        payload = dict(data)

        raw_steps: List[Any] = payload.pop('steps', None) or []
        parsed_steps = [
            step if isinstance(step, Step) else Step(step)
            for step in raw_steps
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

        started_at = _parse_timestamp(payload.pop('started_at', None))
        completed_at = _parse_timestamp(payload.pop('completed_at', None))

        self.data = JobValidator(
            **payload,
            conclusion=parsed_conclusion,
            status=parsed_status,
            steps=parsed_steps,
            started_at=started_at,
            completed_at=completed_at,
        )

        self.name = re.sub(
            r'\s+',
            '',
            self.data.name,
        )

        self.duration: Optional[float] = (
            (self.data.completed_at - self.data.started_at).total_seconds()
            if self.data.started_at is not None and self.data.completed_at is not None
            else None
        )

    @property
    def state(self) -> Status:
        return self.data.status

    @property
    def status(self) -> Optional[Conclusion]:
        return self.data.conclusion
