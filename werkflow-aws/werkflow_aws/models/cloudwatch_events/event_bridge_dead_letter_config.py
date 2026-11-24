from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeadLetterConfig(BaseModel):
    Arn: StrictStr | None = None
