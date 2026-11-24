from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitApproval(BaseModel):
    userArn: StrictStr | None = None
    approvalState: StrictStr | None = None
