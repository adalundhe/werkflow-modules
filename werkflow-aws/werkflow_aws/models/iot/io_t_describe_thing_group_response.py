from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_thing_group_metadata import IoTThingGroupMetadata
from .io_t_thing_group_properties import IoTThingGroupProperties


class IoTDescribeThingGroupResponse(BaseModel):
    thingGroupName: StrictStr | None = None
    thingGroupId: StrictStr | None = None
    thingGroupArn: StrictStr | None = None
    version: StrictInt | None = None
    thingGroupProperties: IoTThingGroupProperties | None = None
    thingGroupMetadata: IoTThingGroupMetadata | None = None
    indexName: StrictStr | None = None
    queryString: StrictStr | None = None
    queryVersion: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
