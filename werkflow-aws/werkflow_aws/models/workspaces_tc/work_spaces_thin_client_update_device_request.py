from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientUpdateDeviceRequest(BaseModel):
    id: StrictStr
    name: StrictStr | None = None
    desiredSoftwareSetId: StrictStr | None = None
    softwareSetUpdateSchedule: Literal['USE_MAINTENANCE_WINDOW', 'APPLY_IMMEDIATELY'] | None = None
