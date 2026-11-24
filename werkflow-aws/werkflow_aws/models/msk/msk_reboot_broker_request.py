from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKRebootBrokerRequest(BaseModel):
    BrokerIds: list[StrictStr]
    ClusterArn: StrictStr
