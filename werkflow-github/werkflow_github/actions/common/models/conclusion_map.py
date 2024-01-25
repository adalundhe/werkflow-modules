from typing import Dict, Literal, Union
from .conclusion import Conclusion


class ConclusionMap:

    def __init__(self) -> None:
        self._types: Dict[
            Union[
                Literal[
                    'success',
                    'failure',
                    'neutral',
                    'cancelled',
                    'skipped',
                    'timed_out',
                    'action_required'
                ],
                None
            ],
            Conclusion
        ] = {
            'success': Conclusion.SUCCESS,
            'failure': Conclusion.FAILURE,
            'neutral': Conclusion.NEUTRAL,
            'cancelled': Conclusion.CANCELLED,
            'skipped': Conclusion.SKIPPED,
            'timed_out': Conclusion.TIMED_OUT,
            'action_required': Conclusion.ACTION_REQUIRED,
            None: Conclusion.UNKNOWN
        }

        self._reverse_map: Dict[
            Conclusion,
            Union[
                Literal[
                    'success',
                    'failure',
                    'neutral',
                    'cancelled',
                    'skipped',
                    'timed_out',
                    'action_required'
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
                'success',
                'failure',
                'neutral',
                'cancelled',
                'skipped',
                'timed_out',
                'action_required'
            ],
            None
        ]
    ):
        return self._types.get(
            job_status,
            Conclusion.UNKNOWN
        )
    
    def get(
        self,
        job_status: Union[
            Literal[
                'success',
                'failure',
                'neutral',
                'cancelled',
                'skipped',
                'timed_out',
                'action_required'
            ],
            None
        ]         
    ):
        return self._types.get(job_status)
    
    def map_to_github_literal(
        self,
        job_status: Conclusion
    ):
        return self._reverse_map.get(job_status)