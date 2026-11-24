from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitApprovalRuleEventMetadata(BaseModel):
    approvalRuleName: StrictStr | None = None
    approvalRuleId: StrictStr | None = None
    approvalRuleContent: StrictStr | None = None
