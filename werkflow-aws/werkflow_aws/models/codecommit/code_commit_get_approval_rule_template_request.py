from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitGetApprovalRuleTemplateRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
