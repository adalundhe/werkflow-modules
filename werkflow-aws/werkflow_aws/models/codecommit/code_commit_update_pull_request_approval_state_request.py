from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitUpdatePullRequestApprovalStateRequest(BaseModel):
    pullRequestId: StrictStr
    revisionId: StrictStr
    approvalState: Literal['APPROVE', 'REVOKE']
