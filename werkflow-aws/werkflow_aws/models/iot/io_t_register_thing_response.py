from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTRegisterThingResponse(BaseModel):
    certificatePem: StrictStr | None = None
    resourceArns: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
