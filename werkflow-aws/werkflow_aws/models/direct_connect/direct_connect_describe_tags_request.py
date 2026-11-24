from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectDescribeTagsRequest(BaseModel):
    resourceArns: list[StrictStr]
