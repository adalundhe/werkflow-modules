from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTRegisterThingRequest(BaseModel):
    templateBody: StrictStr
    parameters: dict[StrictStr, StrictStr] | None = None
