from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitPullRequestCreatedEventMetadata(BaseModel):
    repositoryName: StrictStr | None = None
    sourceCommitId: StrictStr | None = None
    destinationCommitId: StrictStr | None = None
    mergeBase: StrictStr | None = None
