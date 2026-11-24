from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQDataReplicationCounterpart(BaseModel):
    BrokerId: StrictStr | None = None
    Region: StrictStr | None = None
