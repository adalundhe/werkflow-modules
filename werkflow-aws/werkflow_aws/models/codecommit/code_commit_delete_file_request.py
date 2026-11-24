from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCommitDeleteFileRequest(BaseModel):
    repositoryName: StrictStr
    branchName: StrictStr
    filePath: StrictStr
    parentCommitId: StrictStr
    keepEmptyFolders: StrictBool | None = None
    commitMessage: StrictStr | None = None
    name: StrictStr | None = None
    email: StrictStr | None = None
