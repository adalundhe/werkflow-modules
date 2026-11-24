from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .support_date_interval import SupportDateInterval
from .supported_hour import SupportedHour


class SupportCommunicationTypeOptions(BaseModel):
    type: StrictStr | None = None
    supportedHours: list[SupportedHour] | None = None
    datesWithoutSupport: list[SupportDateInterval] | None = None
