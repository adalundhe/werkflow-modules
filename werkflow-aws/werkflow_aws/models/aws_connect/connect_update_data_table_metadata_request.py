from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateDataTableMetadataRequest(BaseModel):
    InstanceId: StrictStr
    DataTableId: StrictStr
    Name: StrictStr
    ValueLockLevel: Literal['NONE', 'DATA_TABLE', 'PRIMARY_VALUE', 'ATTRIBUTE', 'VALUE']
    TimeZone: StrictStr
    Description: StrictStr | None = None
