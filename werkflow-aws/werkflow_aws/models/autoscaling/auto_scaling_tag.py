from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingTag(BaseModel):
    Key: StrictStr
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Value: StrictStr | None = None
    PropagateAtLaunch: StrictBool | None = None
