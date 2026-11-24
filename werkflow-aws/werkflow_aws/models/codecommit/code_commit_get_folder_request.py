from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetFolderRequest(BaseModel):
    repositoryName: StrictStr
    folderPath: StrictStr
    commitSpecifier: StrictStr | None = None
