from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitMergeHunkDetail(BaseModel):
    startLine: StrictInt | None = None
    endLine: StrictInt | None = None
    hunkContent: StrictStr | None = None
