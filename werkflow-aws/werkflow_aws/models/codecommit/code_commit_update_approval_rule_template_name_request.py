from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateApprovalRuleTemplateNameRequest(BaseModel):
    oldApprovalRuleTemplateName: StrictStr
    newApprovalRuleTemplateName: StrictStr
