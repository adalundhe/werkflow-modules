from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateThingGroupResponse(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupArn: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
