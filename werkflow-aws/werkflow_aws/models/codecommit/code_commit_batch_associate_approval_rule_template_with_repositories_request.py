from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchAssociateApprovalRuleTemplateWithRepositoriesRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    repositoryNames: list[StrictStr]
