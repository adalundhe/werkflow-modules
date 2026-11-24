from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQBrokerInstance(BaseModel):
    ConsoleURL: StrictStr | None = None
    Endpoints: list[StrictStr] | None = None
    IpAddress: StrictStr | None = None
