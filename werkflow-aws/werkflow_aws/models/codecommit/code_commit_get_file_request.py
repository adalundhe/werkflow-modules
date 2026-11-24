from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetFileRequest(BaseModel):
    repositoryName: StrictStr
    filePath: StrictStr
    commitSpecifier: StrictStr | None = None
