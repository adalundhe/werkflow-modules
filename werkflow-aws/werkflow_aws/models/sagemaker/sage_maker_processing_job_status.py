from __future__ import annotations
from typing import Literal


SageMakerProcessingJobStatus = Literal[
    'InProgress',
    'Completed',
    'Failed',
    'Stopping',
    'Stopped',
]
