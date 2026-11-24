from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitGetMergeCommitResponse(BaseModel):
    sourceCommitId: StrictStr | None = None
    destinationCommitId: StrictStr | None = None
    baseCommitId: StrictStr | None = None
    mergedCommitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
