from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRPlacementGroupConfig(BaseModel):
    InstanceRole: StrictStr | None = None
    PlacementStrategy: StrictStr | None = None
