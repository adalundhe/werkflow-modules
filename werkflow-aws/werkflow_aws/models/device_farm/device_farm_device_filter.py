from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmDeviceFilter(BaseModel):
    attribute: StrictStr | None = None
    operator: StrictStr | None = None
    values: list[StrictStr] | None = None
