from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeCommitUpdatePullRequestStatusRequest(BaseModel):
    pullRequestId: StrictStr
    pullRequestStatus: Literal['OPEN', 'CLOSED']
