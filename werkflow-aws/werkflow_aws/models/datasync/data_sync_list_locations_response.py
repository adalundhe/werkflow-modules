from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_location_list_entry import DataSyncLocationListEntry


class DataSyncListLocationsResponse(BaseModel):
    Locations: list[DataSyncLocationListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
