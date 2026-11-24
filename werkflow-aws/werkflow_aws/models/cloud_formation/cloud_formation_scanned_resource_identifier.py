from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationScannedResourceIdentifier(BaseModel):
    ResourceType: StrictStr
    ResourceIdentifier: dict[StrictStr, StrictStr]
