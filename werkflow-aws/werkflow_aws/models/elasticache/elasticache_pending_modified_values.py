from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Literal
from .elasticache_log_delivery_configuration import ElasticacheLogDeliveryConfiguration


class ElasticachePendingModifiedValues(BaseModel):
    NumCacheNodes: StrictInt
    CacheNodeIdsToRemove: list[StrictStr]
    EngineVersion: StrictStr
    CacheNodeType: StrictStr
    AuthTokenStatus: Literal['SETTING', 'ROTATING']
    LogDeliveryConfigruations: list[ElasticacheLogDeliveryConfiguration]
    TransitEncryptionEnabled: StrictBool
    TransitEncryptionMode: Literal['preferred', 'required']