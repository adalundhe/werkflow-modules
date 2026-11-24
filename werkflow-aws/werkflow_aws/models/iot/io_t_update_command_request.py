from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTUpdateCommandRequest(BaseModel):
    commandId: StrictStr
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    deprecated: StrictBool | None = None
