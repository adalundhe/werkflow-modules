from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeCommitMergeMetadata(BaseModel):
    isMerged: StrictBool | None = None
    mergedBy: StrictStr | None = None
    mergeCommitId: StrictStr | None = None
    mergeOption: StrictStr | None = None
