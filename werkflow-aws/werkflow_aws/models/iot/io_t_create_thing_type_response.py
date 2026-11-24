from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateThingTypeResponse(BaseModel):
    thingTypeName: StrictStr | None = None
    thingTypeArn: StrictStr | None = None
    thingTypeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
