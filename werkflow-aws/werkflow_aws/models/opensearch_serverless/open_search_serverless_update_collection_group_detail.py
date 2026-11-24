from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_collection_group_capacity_limits import OpenSearchServerlessCollectionGroupCapacityLimits


class OpenSearchServerlessUpdateCollectionGroupDetail(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    capacityLimits: OpenSearchServerlessCollectionGroupCapacityLimits | None = None
    createdDate: StrictInt | None = None
    lastModifiedDate: StrictInt | None = None
    generation: StrictStr | None = None
