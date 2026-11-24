from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetBlobRequest(BaseModel):
    repositoryName: StrictStr
    blobId: StrictStr
