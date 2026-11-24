from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTAttributePayload(BaseModel):
    attributes: dict[StrictStr, StrictStr] | None = None
    merge: StrictBool | None = None
