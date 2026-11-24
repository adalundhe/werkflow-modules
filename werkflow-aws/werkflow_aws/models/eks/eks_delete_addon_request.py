from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSDeleteAddonRequest(BaseModel):
    clusterName: StrictStr
    addonName: StrictStr
    preserve: StrictBool | None = None
