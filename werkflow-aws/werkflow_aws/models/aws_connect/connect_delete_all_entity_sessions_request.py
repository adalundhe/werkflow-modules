from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDeleteAllEntitySessionsRequest(BaseModel):
    InstanceId: StrictStr
    EntityId: StrictStr
    EntityType: Literal['USER']
