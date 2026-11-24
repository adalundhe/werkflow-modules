from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointWriteEventStream(BaseModel):
    DestinationStreamArn: StrictStr
    RoleArn: StrictStr
