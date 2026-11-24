from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmRule(BaseModel):
    attribute: StrictStr | None = None
    operator: StrictStr | None = None
    value: StrictStr | None = None
