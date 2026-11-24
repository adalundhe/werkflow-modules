from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitLocation(BaseModel):
    filePath: StrictStr | None = None
    filePosition: StrictInt | None = None
    relativeFileVersion: StrictStr | None = None
