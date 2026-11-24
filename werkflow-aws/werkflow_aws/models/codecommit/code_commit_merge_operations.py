from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitMergeOperations(BaseModel):
    source: StrictStr | None = None
    destination: StrictStr | None = None
