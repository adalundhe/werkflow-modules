from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruCommitDiffSourceCodeType(BaseModel):
    SourceCommit: StrictStr | None = None
    DestinationCommit: StrictStr | None = None
    MergeBaseCommit: StrictStr | None = None
