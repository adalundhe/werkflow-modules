from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_serverless_collection_group_capacity_limits import OpenSearchServerlessCollectionGroupCapacityLimits
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessCreateCollectionGroupRequest(BaseModel):
    name: StrictStr
    standbyReplicas: Literal['ENABLED', 'DISABLED']
    description: StrictStr | None = None
    tags: list[OpenSearchServerlessTag] | None = None
    capacityLimits: OpenSearchServerlessCollectionGroupCapacityLimits | None = None
    generation: Literal['CLASSIC', 'NEXTGEN'] | None = None
    clientToken: StrictStr | None = None
