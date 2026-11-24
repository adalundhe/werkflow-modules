from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AppSyncApiCache(BaseModel):
    ttl: StrictInt | None = None
    apiCachingBehavior: StrictStr | None = None
    transitEncryptionEnabled: StrictBool | None = None
    atRestEncryptionEnabled: StrictBool | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    healthMetricsConfig: StrictStr | None = None
