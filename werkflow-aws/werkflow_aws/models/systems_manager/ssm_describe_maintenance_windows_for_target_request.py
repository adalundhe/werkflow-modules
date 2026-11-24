from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_target import SSMTarget


class SSMDescribeMaintenanceWindowsForTargetRequest(BaseModel):
    Targets: list[SSMTarget]
    ResourceType: Literal['INSTANCE', 'RESOURCE_GROUP']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
