from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitCreatePullRequestApprovalRuleRequest(BaseModel):
    pullRequestId: StrictStr
    approvalRuleName: StrictStr
    approvalRuleContent: StrictStr
