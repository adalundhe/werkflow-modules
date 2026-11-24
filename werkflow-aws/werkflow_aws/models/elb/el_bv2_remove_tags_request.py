from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2RemoveTagsRequest(BaseModel):
    ResourceArns: list[StrictStr]
    TagKeys: list[StrictStr]
