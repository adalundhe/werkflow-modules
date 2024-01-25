from typing import Dict, Union, Literal
from  .status import Status


class StatusMap:

    def __init__(self) -> None:
        self._types: Dict[
            Union[
                Literal[
                    'queued',
                    'in_progress',
                    'completed',
                    'waiting'
                ],
                None
            ],
            Status
        ] = {
            'queued': Status.QUEUED,
            'in_progress': Status.IN_PROGRESS,
            'completed': Status.COMPLETED,
            'waiting': Status.WAITING
        }

        self._reverse_map: Dict[
            Status,
            Union[
                Literal[
                    'queued',
                    'in_progress',
                    'completed',
                    'waiting'
                ],
                None
            ]
        ] = {
            value: key for key, value in self._types.items()
        }

    def __getitem__(
        self,
        job_status: Union[
            Literal[
                'queued',
                'in_progress',
                'completed',
                'waiting'
            ],
            None
        ]
    ):
        return self._types.get(
            job_status,
            Status.QUEUED
        )
    
    def get(
        self,
        job_status: Union[
            Literal[
                'queued',
                'in_progress',
                'completed',
                'waiting'
            ],
            None
        ]         
    ):
        return self._types.get(job_status)
    
    def map_to_github_literal(
        self,
        job_status: Status
    ):
        return self._reverse_map.get(job_status)