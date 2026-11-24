from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitOverridePullRequestApprovalRulesRequest(BaseModel):
    pullRequestId: StrictStr
    revisionId: StrictStr
    overrideStatus: Literal['OVERRIDE', 'REVOKE']
