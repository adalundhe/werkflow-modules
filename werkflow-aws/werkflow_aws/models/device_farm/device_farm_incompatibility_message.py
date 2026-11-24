from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmIncompatibilityMessage(BaseModel):
    message: StrictStr | None = None
    type: StrictStr | None = None
