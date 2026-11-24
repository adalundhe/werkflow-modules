from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitPullRequestSourceReferenceUpdatedEventMetadata(BaseModel):
    repositoryName: StrictStr | None = None
    beforeCommitId: StrictStr | None = None
    afterCommitId: StrictStr | None = None
    mergeBase: StrictStr | None = None
