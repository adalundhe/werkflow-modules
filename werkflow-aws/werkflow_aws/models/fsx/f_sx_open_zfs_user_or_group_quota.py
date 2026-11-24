from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxOpenZFSUserOrGroupQuota(BaseModel):
    Type: StrictStr | None = None
    Id: StrictInt | None = None
    StorageCapacityQuotaGiB: StrictInt | None = None
