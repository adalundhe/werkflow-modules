from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationChangeSetHookResourceTargetDetails(BaseModel):
    LogicalResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceAction: StrictStr | None = None
