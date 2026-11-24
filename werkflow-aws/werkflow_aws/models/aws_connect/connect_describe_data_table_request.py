from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeDataTableRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
