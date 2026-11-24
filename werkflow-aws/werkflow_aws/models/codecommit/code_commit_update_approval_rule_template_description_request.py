from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateApprovalRuleTemplateDescriptionRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    approvalRuleTemplateDescription: StrictStr
