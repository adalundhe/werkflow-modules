from __future__ import annotations
from pydantic import BaseModel
from .data_zone_account_info import DataZoneAccountInfo
from .data_zone_custom_account_pool_handler import DataZoneCustomAccountPoolHandler


class DataZoneAccountSource(BaseModel):
    accounts: list[DataZoneAccountInfo] | None = None
    customAccountPoolHandler: DataZoneCustomAccountPoolHandler | None = None
