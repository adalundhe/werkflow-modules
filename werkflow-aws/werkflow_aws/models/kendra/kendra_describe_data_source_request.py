from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeDataSourceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
