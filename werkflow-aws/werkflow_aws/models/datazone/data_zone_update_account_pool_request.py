from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_account_source import DataZoneAccountSource


class DataZoneUpdateAccountPoolRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    resolutionStrategy: Literal['MANUAL'] | None = None
    accountSource: DataZoneAccountSource | None = None
