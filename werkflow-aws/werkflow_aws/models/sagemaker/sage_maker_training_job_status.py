from __future__ import annotations
from typing import Literal


SageMakerTrainingJobStatus = Literal[
    'InProgress',
    'Completed',
    'Failed',
    'Stopping',
    'Stopped',
    'Deleting',
]
