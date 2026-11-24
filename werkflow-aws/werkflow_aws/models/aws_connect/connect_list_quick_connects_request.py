from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListQuickConnectsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    QuickConnectTypes: list[Literal['USER', 'QUEUE', 'PHONE_NUMBER', 'FLOW']] | None = None
