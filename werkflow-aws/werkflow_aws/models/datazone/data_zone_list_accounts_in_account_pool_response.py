from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_account_info import DataZoneAccountInfo


class DataZoneListAccountsInAccountPoolResponse(BaseModel):
    items: list[DataZoneAccountInfo] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
