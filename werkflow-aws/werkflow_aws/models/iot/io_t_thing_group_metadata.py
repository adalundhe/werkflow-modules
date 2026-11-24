from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_group_name_and_arn import IoTGroupNameAndArn


class IoTThingGroupMetadata(BaseModel):
    parentGroupName: StrictStr | None = None
    rootToParentThingGroups: list[IoTGroupNameAndArn] | None = None
    creationDate: datetime.datetime | StrictStr | None = None
