from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaCallbackStartedDetails(BaseModel):
    CallbackId: StrictStr | None = None
    HeartbeatTimeout: StrictInt | None = None
    Timeout: StrictInt | None = None
