from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitDisassociateApprovalRuleTemplateFromRepositoryRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    repositoryName: StrictStr
