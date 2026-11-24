from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateThingResponse(BaseModel):
    thingName: StrictStr | None = None
    thingArn: StrictStr | None = None
    thingId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
