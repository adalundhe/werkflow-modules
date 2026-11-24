from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDescribeBrokerRequest(BaseModel):
    BrokerId: StrictStr
