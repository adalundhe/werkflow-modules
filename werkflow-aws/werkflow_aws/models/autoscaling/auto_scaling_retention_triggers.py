from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingRetentionTriggers(BaseModel):
    TerminateHookAbandon: StrictStr | None = None
