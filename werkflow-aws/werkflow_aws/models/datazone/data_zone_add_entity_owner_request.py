from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_owner_properties import DataZoneOwnerProperties


class DataZoneAddEntityOwnerRequest(BaseModel):
    domainIdentifier: StrictStr
    entityType: Literal['DOMAIN_UNIT']
    entityIdentifier: StrictStr
    owner: DataZoneOwnerProperties
    clientToken: StrictStr | None = None
