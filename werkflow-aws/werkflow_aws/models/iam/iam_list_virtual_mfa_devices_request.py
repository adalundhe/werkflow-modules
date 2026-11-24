from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListVirtualMFADevicesRequest(BaseModel):
    AssignmentStatus: Literal['Assigned', 'Unassigned', 'Any'] | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
