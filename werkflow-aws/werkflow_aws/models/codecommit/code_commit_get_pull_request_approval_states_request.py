from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetPullRequestApprovalStatesRequest(BaseModel):
    pullRequestId: StrictStr
    revisionId: StrictStr
