from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_collection_group_capacity_limits import OpenSearchServerlessCollectionGroupCapacityLimits


class OpenSearchServerlessUpdateCollectionGroupRequest(BaseModel):
    id: StrictStr
    description: StrictStr | None = None
    capacityLimits: OpenSearchServerlessCollectionGroupCapacityLimits | None = None
    clientToken: StrictStr | None = None
