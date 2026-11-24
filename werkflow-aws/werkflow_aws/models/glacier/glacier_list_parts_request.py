from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListPartsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    uploadId: StrictStr
    marker: StrictStr | None = None
    limit: StrictStr | None = None
