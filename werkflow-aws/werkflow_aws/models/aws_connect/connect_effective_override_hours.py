from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_override_hour import ConnectOverrideHour


class ConnectEffectiveOverrideHours(BaseModel):
    Date: StrictStr | None = None
    OverrideHours: list[ConnectOverrideHour] | None = None
