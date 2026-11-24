from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2InstanceTagNotificationAttribute(BaseModel):
    InstanceTagKeys: list[StrictStr] | None = None
    IncludeAllTagsOfInstance: StrictBool | None = None
