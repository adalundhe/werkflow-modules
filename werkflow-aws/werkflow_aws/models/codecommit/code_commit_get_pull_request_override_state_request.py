from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetPullRequestOverrideStateRequest(BaseModel):
    pullRequestId: StrictStr
    revisionId: StrictStr
