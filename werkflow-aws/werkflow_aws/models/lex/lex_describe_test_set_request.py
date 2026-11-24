from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeTestSetRequest(BaseModel):
    testSetId: StrictStr
