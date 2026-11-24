from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_reject_choice import DataZoneRejectChoice
from .data_zone_reject_rule import DataZoneRejectRule


class DataZoneRejectPredictionsRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    revision: StrictStr | None = None
    rejectRule: DataZoneRejectRule | None = None
    rejectChoices: list[DataZoneRejectChoice] | None = None
    clientToken: StrictStr | None = None
