from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeIndexRequest(BaseModel):
    Id: StrictStr
