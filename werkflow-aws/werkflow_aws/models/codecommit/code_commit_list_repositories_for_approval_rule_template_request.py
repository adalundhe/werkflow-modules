from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitListRepositoriesForApprovalRuleTemplateRequest(BaseModel):
    approvalRuleTemplateName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
