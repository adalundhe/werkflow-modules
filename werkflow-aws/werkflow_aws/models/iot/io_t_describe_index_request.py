from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeIndexRequest(BaseModel):
    indexName: StrictStr
