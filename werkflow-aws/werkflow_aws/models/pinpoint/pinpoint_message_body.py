from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointMessageBody(BaseModel):
    Message: StrictStr | None = None
    RequestID: StrictStr | None = None
