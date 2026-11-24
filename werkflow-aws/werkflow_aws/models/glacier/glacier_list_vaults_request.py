from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListVaultsRequest(BaseModel):
    accountId: StrictStr
    marker: StrictStr | None = None
    limit: StrictStr | None = None
