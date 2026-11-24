from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteTagsRequest(BaseModel):
    ResourceName: StrictStr
    TagKeys: list[StrictStr]
