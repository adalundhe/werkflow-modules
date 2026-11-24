from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitDeletePullRequestApprovalRuleResponse(BaseModel):
    approvalRuleId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
