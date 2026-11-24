from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_file_version import CodeCommitFileVersion


class CodeCommitListFileCommitHistoryResponse(BaseModel):
    revisionDag: list[CodeCommitFileVersion] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
