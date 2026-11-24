from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteDataTableRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
