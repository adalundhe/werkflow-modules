from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AutoScalingTagDescription(BaseModel):
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    PropagateAtLaunch: StrictBool | None = None
