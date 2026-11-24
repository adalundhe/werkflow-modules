from __future__ import annotations
from typing import Literal


SageMakerNotebookInstanceStatus = Literal[
    'Pending',
    'InService',
    'Stopping',
    'Stopped',
    'Failed',
    'Deleting',
    'Updating',
    'PendingMaintenance',
    'InMaintenance',
]
