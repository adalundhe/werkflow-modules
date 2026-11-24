from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationResourceToImport(BaseModel):
    ResourceType: StrictStr
    LogicalResourceId: StrictStr
    ResourceIdentifier: dict[StrictStr, StrictStr]
