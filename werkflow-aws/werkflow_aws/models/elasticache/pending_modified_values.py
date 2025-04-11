from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import Literal
from .log_delivery_configuration import LogDeliveryConfiguration


class PendingModifiedValues(BaseModel):
    NumCacheNodes: StrictInt
    CacheNodeIdsToRemove: list[StrictStr]
    EngineVersion: StrictStr
    CacheNodeType: StrictStr
    AuthTokenStatus: Literal['SETTING', 'ROTATING']
    LogDeliveryConfigruations: list[LogDeliveryConfiguration]
    TransitEncryptionEnabled: StrictBool
    TransitEncryptionMode: Literal['preferred', 'required']