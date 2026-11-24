from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_merge_metadata import CodeCommitMergeMetadata


class CodeCommitPullRequestMergedStateChangedEventMetadata(BaseModel):
    repositoryName: StrictStr | None = None
    destinationReference: StrictStr | None = None
    mergeMetadata: CodeCommitMergeMetadata | None = None
