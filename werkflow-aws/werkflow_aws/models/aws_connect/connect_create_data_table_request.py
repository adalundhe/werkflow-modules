from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreateDataTableRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    TimeZone: StrictStr
    ValueLockLevel: Literal['NONE', 'DATA_TABLE', 'PRIMARY_VALUE', 'ATTRIBUTE', 'VALUE']
    Status: Literal['PUBLISHED']
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
