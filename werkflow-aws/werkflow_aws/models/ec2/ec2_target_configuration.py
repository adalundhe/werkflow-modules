from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TargetConfiguration(BaseModel):
    InstanceCount: StrictInt | None = None
    OfferingId: StrictStr | None = None
