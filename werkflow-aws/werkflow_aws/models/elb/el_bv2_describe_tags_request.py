from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2DescribeTagsRequest(BaseModel):
    ResourceArns: list[StrictStr]
