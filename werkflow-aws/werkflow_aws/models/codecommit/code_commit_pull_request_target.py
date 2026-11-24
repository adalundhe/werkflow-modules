from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_merge_metadata import CodeCommitMergeMetadata


class CodeCommitPullRequestTarget(BaseModel):
    repositoryName: StrictStr | None = None
    sourceReference: StrictStr | None = None
    destinationReference: StrictStr | None = None
    destinationCommit: StrictStr | None = None
    sourceCommit: StrictStr | None = None
    mergeBase: StrictStr | None = None
    mergeMetadata: CodeCommitMergeMetadata | None = None
