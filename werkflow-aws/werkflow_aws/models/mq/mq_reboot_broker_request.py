from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQRebootBrokerRequest(BaseModel):
    BrokerId: StrictStr
