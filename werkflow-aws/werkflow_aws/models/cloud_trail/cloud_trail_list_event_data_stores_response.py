from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_event_data_store import CloudTrailEventDataStore


class CloudTrailListEventDataStoresResponse(BaseModel):
    EventDataStores: list[CloudTrailEventDataStore] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
