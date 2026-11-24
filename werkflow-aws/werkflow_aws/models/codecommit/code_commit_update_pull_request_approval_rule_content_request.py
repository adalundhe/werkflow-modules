from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdatePullRequestApprovalRuleContentRequest(BaseModel):
    pullRequestId: StrictStr
    approvalRuleName: StrictStr
    newRuleContent: StrictStr
    existingRuleContentSha256: StrictStr | None = None
