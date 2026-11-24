from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeSqsParameters(BaseModel):
    MessageGroupId: StrictStr | None = None
