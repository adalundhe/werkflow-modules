from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateDynamicThingGroupResponse(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupArn: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    indexName: StrictStr | None = None
    queryString: StrictStr | None = None
    queryVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
