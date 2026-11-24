from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitFile(BaseModel):
    blobId: StrictStr | None = None
    absolutePath: StrictStr | None = None
    relativePath: StrictStr | None = None
    fileMode: StrictStr | None = None
