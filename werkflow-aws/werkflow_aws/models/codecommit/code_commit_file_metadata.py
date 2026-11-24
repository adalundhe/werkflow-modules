from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitFileMetadata(BaseModel):
    absolutePath: StrictStr | None = None
    blobId: StrictStr | None = None
    fileMode: StrictStr | None = None
