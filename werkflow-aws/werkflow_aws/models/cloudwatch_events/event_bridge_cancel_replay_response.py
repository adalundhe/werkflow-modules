from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeCancelReplayResponse(BaseModel):
    ReplayArn: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
