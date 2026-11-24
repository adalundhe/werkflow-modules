from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration


class ElasticachePendingModifiedValues(BaseModel):
    NumCacheNodes: StrictInt | None = None
    CacheNodeIdsToRemove: list[StrictStr] | None = None
    EngineVersion: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    AuthTokenStatus: Literal['SETTING', 'ROTATING'] | None = None
    LogDeliveryConfigurations: list[ElasticacheLogDeliveryConfiguration] | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    TransitEncryptionMode: Literal['preferred', 'required'] | None = None
