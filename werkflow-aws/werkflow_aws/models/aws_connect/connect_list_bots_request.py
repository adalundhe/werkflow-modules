from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListBotsRequest(BaseModel):
    InstanceId: StrictStr
    LexVersion: Literal['V1', 'V2']
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
