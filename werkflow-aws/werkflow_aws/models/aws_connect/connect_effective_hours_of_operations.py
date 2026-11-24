from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_operational_hour import ConnectOperationalHour


class ConnectEffectiveHoursOfOperations(BaseModel):
    Date: StrictStr | None = None
    OperationalHours: list[ConnectOperationalHour] | None = None
