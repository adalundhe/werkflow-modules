from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_account_source import DataZoneAccountSource


class DataZoneCreateAccountPoolRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    resolutionStrategy: Literal['MANUAL']
    accountSource: DataZoneAccountSource
    description: StrictStr | None = None
