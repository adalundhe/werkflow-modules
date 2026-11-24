from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitDeletePullRequestApprovalRuleRequest(BaseModel):
    pullRequestId: StrictStr
    approvalRuleName: StrictStr
