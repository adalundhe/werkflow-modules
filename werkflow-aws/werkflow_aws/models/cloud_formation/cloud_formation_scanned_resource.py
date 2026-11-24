from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationScannedResource(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceIdentifier: dict[StrictStr, StrictStr] | None = None
    ManagedByStack: StrictBool | None = None
