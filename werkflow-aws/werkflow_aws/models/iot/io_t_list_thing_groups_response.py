from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_group_name_and_arn import IoTGroupNameAndArn


class IoTListThingGroupsResponse(BaseModel):
    thingGroups: list[IoTGroupNameAndArn] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
