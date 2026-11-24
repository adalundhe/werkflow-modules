from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_warning_detail import CloudFormationWarningDetail


class CloudFormationResourceDetail(BaseModel):
    ResourceType: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    ResourceIdentifier: dict[StrictStr, StrictStr] | None = None
    ResourceStatus: StrictStr | None = None
    ResourceStatusReason: StrictStr | None = None
    Warnings: list[CloudFormationWarningDetail] | None = None
