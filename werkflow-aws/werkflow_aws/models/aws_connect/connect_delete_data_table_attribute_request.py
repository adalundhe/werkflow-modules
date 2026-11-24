from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteDataTableAttributeRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    AttributeName: StrictStr
