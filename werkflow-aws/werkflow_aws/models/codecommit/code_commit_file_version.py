from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_commit import CodeCommitCommit


class CodeCommitFileVersion(BaseModel):
    commit: CodeCommitCommit | None = None
    blobId: StrictStr | None = None
    path: StrictStr | None = None
    revisionChildren: list[StrictStr] | None = None
