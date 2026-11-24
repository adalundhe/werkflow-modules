from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeClientPropertiesRequest(BaseModel):
    ResourceIds: list[StrictStr]
