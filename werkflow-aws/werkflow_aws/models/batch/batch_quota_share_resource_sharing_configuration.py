from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchQuotaShareResourceSharingConfiguration(BaseModel):
    strategy: StrictStr | None = None
    borrowLimit: StrictInt | None = None
