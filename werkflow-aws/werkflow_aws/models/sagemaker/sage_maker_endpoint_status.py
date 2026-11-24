from __future__ import annotations
from typing import Literal


SageMakerEndpointStatus = Literal[
    'OutOfService',
    'Creating',
    'Updating',
    'SystemUpdating',
    'RollingBack',
    'InService',
    'Deleting',
    'Failed',
    'UpdateRollbackFailed',
]
