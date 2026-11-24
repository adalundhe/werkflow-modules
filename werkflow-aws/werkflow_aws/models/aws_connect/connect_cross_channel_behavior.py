from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCrossChannelBehavior(BaseModel):
    BehaviorType: StrictStr | None = None
