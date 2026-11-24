from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitAssociateApprovalRuleTemplateWithRepositoryRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    repositoryName: StrictStr
