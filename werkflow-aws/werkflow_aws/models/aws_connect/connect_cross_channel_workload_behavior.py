from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCrossChannelWorkloadBehavior(BaseModel):
    ChannelWorkloadBehaviorType: StrictStr | None = None
