from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBlobMetadata(BaseModel):
    blobId: StrictStr | None = None
    path: StrictStr | None = None
    mode: StrictStr | None = None
