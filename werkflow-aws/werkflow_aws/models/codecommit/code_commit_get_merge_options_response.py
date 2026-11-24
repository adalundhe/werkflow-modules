from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitGetMergeOptionsResponse(BaseModel):
    mergeOptions: list[StrictStr] | None = None
    sourceCommitId: StrictStr | None = None
    destinationCommitId: StrictStr | None = None
    baseCommitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
