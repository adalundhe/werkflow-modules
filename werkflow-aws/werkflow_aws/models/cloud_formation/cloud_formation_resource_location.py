from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationResourceLocation(BaseModel):
    StackName: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
