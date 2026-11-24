from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitListApprovalRuleTemplatesRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
