from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_sync_location_filter import DataSyncLocationFilter


class DataSyncListLocationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filters: list[DataSyncLocationFilter] | None = None
