import datetime
from typing import (
    Dict,
    Union
)
from werkflow_github.actions.common.models import (
    ConclusionMap,
    StatusMap
)
from .step_validator import StepValidator


class Step:

    def __init__(
        self,
        data: Dict[
            str,
            Union[str, int]
        ]
    ) -> None:
        self._status_map = StatusMap()
        self._conclusion_map = ConclusionMap()
        self.data = StepValidator(
            **data,
            conclusion=self._conclusion_map.get(
                data.get('conclusion')
            ),
            status=self._conclusion_map.get(
                data.get('status')
            ),
            started_at=datetime.datetime.strptime(
                data.get('started_at'),
                '%Y-%m-%dT%H:%M:%SZ'
            ),
            completed_at=datetime.datetime.strptime(
                data.get('completed_at'),
                '%Y-%m-%dT%H:%M:%SZ'
            )
        )