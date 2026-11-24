from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitPullRequestStatusChangedEventMetadata(BaseModel):
    pullRequestStatus: StrictStr | None = None
