from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierInitiateMultipartUploadRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    archiveDescription: StrictStr | None = None
    partSize: StrictStr | None = None
