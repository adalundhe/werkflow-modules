from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListLexBotsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
