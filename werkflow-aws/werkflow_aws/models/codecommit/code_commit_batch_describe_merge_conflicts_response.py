from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_commit_batch_describe_merge_conflicts_error import CodeCommitBatchDescribeMergeConflictsError
from .code_commit_conflict import CodeCommitConflict


class CodeCommitBatchDescribeMergeConflictsResponse(BaseModel):
    conflicts: list[CodeCommitConflict] | None = None
    nextToken: StrictStr | None = None
    errors: list[CodeCommitBatchDescribeMergeConflictsError] | None = None
    destinationCommitId: StrictStr | None = None
    sourceCommitId: StrictStr | None = None
    baseCommitId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
