from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateApprovalRuleTemplateContentRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    newRuleContent: StrictStr
    existingRuleContentSha256: StrictStr | None = None
