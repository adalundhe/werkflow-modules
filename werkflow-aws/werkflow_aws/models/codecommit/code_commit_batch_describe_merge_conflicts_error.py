from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchDescribeMergeConflictsError(BaseModel):
    filePath: StrictStr | None = None
    exceptionName: StrictStr | None = None
    message: StrictStr | None = None
