from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierCompleteMultipartUploadRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    uploadId: StrictStr
    archiveSize: StrictStr | None = None
    checksum: StrictStr | None = None
