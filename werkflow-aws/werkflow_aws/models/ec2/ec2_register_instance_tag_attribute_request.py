from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RegisterInstanceTagAttributeRequest(BaseModel):
    IncludeAllTagsOfInstance: StrictBool | None = None
    InstanceTagKeys: list[StrictStr] | None = None
