from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayPoolInfo(BaseModel):
    PoolARN: StrictStr | None = None
    PoolName: StrictStr | None = None
    StorageClass: StrictStr | None = None
    RetentionLockType: StrictStr | None = None
    RetentionLockTimeInDays: StrictInt | None = None
    PoolStatus: StrictStr | None = None
