from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitApprovalRuleOverriddenEventMetadata(BaseModel):
    revisionId: StrictStr | None = None
    overrideStatus: StrictStr | None = None
