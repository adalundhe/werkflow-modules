from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDescribeThingResponse(BaseModel):
    defaultClientId: StrictStr | None = None
    thingName: StrictStr | None = None
    thingId: StrictStr | None = None
    thingArn: StrictStr | None = None
    thingTypeName: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    version: StrictInt | None = None
    billingGroupName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
