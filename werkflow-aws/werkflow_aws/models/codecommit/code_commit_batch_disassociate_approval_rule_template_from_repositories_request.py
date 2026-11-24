from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitBatchDisassociateApprovalRuleTemplateFromRepositoriesRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    repositoryNames: list[StrictStr]
