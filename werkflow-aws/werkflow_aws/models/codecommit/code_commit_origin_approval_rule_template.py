from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitOriginApprovalRuleTemplate(BaseModel):
    approvalRuleTemplateId: StrictStr | None = None
    approvalRuleTemplateName: StrictStr | None = None
