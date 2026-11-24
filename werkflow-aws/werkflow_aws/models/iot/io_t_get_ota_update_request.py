from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetOTAUpdateRequest(BaseModel):
    otaUpdateId: StrictStr
