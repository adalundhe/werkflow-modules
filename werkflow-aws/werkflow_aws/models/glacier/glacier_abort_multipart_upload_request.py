from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierAbortMultipartUploadRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    uploadId: StrictStr
