from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_accept_choice import DataZoneAcceptChoice
from .data_zone_accept_rule import DataZoneAcceptRule


class DataZoneAcceptPredictionsRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    revision: StrictStr | None = None
    acceptRule: DataZoneAcceptRule | None = None
    acceptChoices: list[DataZoneAcceptChoice] | None = None
    clientToken: StrictStr | None = None
