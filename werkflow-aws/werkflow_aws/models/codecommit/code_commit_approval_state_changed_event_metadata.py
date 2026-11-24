from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitApprovalStateChangedEventMetadata(BaseModel):
    revisionId: StrictStr | None = None
    approvalStatus: StrictStr | None = None
