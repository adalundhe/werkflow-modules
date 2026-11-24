from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitMergeBranchesBySquashResponse(BaseModel):
    commitId: StrictStr | None = None
    treeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
