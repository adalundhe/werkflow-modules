from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListMultipartUploadsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    marker: StrictStr | None = None
    limit: StrictStr | None = None
