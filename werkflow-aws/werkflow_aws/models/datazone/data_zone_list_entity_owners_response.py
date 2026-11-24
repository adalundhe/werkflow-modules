from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_owner_properties_output import DataZoneOwnerPropertiesOutput


class DataZoneListEntityOwnersResponse(BaseModel):
    owners: list[DataZoneOwnerPropertiesOutput] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
