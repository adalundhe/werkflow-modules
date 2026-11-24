from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitEvaluatePullRequestApprovalRulesRequest(BaseModel):
    pullRequestId: StrictStr
    revisionId: StrictStr
