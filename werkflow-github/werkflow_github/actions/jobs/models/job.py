import datetime
import re
from typing import Dict, List, Union
from werkflow_github.actions.common.models import (
    ConclusionMap,
    StatusMap
)
from werkflow_github.actions.steps.models import Step
from .job_validator import JobValidator

class Job:


    def __init__(
        self,
        data: Dict[str, str]
    ) -> None:
        self._status_map = StatusMap()
        self._conclusion_map = ConclusionMap()

        steps: List[Dict[str, Union[int, str]]] = data.get('steps', [])

        self.data = JobValidator(
            **data,
            conclusion=self._conclusion_map.get(
                data.get('conclusion')
            ),
            status=data.get('status'),
            steps=[
                Step(step) for step in steps
            ],
            started_at=datetime.datetime.strptime(
                data.get('started_at'),
                '%Y-%m-%dT%H:%M:%SZ'
            ),
            completed_at=datetime.datetime.strptime(
                data.get('completed_at'),
                '%Y-%m-%dT%H:%M:%SZ'
            )
        )

        self.name = re.sub(
            r"\s+",
            "",
            self.data.name
        )

        self.duration = (
            self.data.completed_at - self.data.started_at
        ).total_seconds()

    @property
    def state(self):
        return self.data.status

    @property
    def status(self):
        return self.data.conclusion
    