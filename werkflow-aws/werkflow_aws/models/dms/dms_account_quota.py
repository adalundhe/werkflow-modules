from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSAccountQuota(BaseModel):
    AccountQuotaName: StrictStr | None = None
    Used: StrictInt | None = None
    Max: StrictInt | None = None
