from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTaskTemplatesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    Name: StrictStr | None = None
