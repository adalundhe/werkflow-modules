from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_destination_details import ElastiCacheDestinationDetails


class ElastiCachePendingLogDeliveryConfiguration(BaseModel):
    LogType: StrictStr | None = None
    DestinationType: StrictStr | None = None
    DestinationDetails: ElastiCacheDestinationDetails | None = None
    LogFormat: StrictStr | None = None
