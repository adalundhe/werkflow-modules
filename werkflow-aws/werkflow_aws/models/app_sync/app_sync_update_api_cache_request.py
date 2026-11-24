from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncUpdateApiCacheRequest(BaseModel):
    apiId: StrictStr
    ttl: StrictInt
    apiCachingBehavior: Literal['FULL_REQUEST_CACHING', 'PER_RESOLVER_CACHING', 'OPERATION_LEVEL_CACHING']
    type: Literal['T2_SMALL', 'T2_MEDIUM', 'R4_LARGE', 'R4_XLARGE', 'R4_2XLARGE', 'R4_4XLARGE', 'R4_8XLARGE', 'SMALL', 'MEDIUM', 'LARGE', 'XLARGE', 'LARGE_2X', 'LARGE_4X', 'LARGE_8X', 'LARGE_12X']
    healthMetricsConfig: Literal['ENABLED', 'DISABLED'] | None = None
