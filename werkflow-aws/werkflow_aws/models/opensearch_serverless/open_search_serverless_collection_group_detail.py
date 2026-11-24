from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_collection_group_capacity_limits import OpenSearchServerlessCollectionGroupCapacityLimits
from .open_search_serverless_current_capacity import OpenSearchServerlessCurrentCapacity
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessCollectionGroupDetail(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    name: StrictStr | None = None
    standbyReplicas: StrictStr | None = None
    description: StrictStr | None = None
    tags: list[OpenSearchServerlessTag] | None = None
    createdDate: StrictInt | None = None
    capacityLimits: OpenSearchServerlessCollectionGroupCapacityLimits | None = None
    currentCapacity: OpenSearchServerlessCurrentCapacity | None = None
    numberOfCollections: StrictInt | None = None
    generation: StrictStr | None = None
