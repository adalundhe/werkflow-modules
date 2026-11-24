from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MQPromoteRequest(BaseModel):
    BrokerId: StrictStr
    Mode: Literal['SWITCHOVER', 'FAILOVER']
