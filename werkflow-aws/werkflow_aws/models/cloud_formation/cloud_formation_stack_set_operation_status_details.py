from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_formation_stages import CloudFormationStages


class CloudFormationStackSetOperationStatusDetails(BaseModel):
    Stages: CloudFormationStages | None = None
    TotalAccountsCount: StrictInt | None = None
    TotalStackInstancesCount: StrictInt | None = None
    FailedStackInstancesCount: StrictInt | None = None
