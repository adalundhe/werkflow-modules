from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetCommandRequest(BaseModel):
    commandId: StrictStr
