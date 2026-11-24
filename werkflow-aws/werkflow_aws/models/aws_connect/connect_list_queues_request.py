from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListQueuesRequest(BaseModel):
    InstanceId: StrictStr
    QueueTypes: list[Literal['STANDARD', 'AGENT']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
