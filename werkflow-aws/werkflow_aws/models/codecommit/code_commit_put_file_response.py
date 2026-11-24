from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitPutFileResponse(BaseModel):
    commitId: StrictStr | None = None
    blobId: StrictStr | None = None
    treeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
