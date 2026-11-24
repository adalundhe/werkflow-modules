from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitMergePullRequestByFastForwardRequest(BaseModel):
    pullRequestId: StrictStr
    repositoryName: StrictStr
    sourceCommitId: StrictStr | None = None
