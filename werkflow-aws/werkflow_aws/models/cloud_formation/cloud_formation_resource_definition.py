from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationResourceDefinition(BaseModel):
    ResourceType: StrictStr
    ResourceIdentifier: dict[StrictStr, StrictStr]
    LogicalResourceId: StrictStr | None = None
