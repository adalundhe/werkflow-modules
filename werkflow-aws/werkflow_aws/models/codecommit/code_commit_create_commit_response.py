from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_file_metadata import CodeCommitFileMetadata


class CodeCommitCreateCommitResponse(BaseModel):
    commitId: StrictStr | None = None
    treeId: StrictStr | None = None
    filesAdded: list[CodeCommitFileMetadata] | None = None
    filesUpdated: list[CodeCommitFileMetadata] | None = None
    filesDeleted: list[CodeCommitFileMetadata] | None = None
    ResponseMetadata: dict[str, Any] | None = None
