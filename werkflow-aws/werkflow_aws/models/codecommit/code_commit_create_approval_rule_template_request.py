from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitCreateApprovalRuleTemplateRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    approvalRuleTemplateContent: StrictStr
    approvalRuleTemplateDescription: StrictStr | None = None
