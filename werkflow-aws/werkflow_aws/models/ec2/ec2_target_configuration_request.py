from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TargetConfigurationRequest(BaseModel):
    OfferingId: StrictStr
    InstanceCount: StrictInt | None = None
