from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_formation_resource_change import CloudFormationResourceChange


class CloudFormationChange(BaseModel):
    Type: StrictStr | None = None
    HookInvocationCount: StrictInt | None = None
    ResourceChange: CloudFormationResourceChange | None = None
