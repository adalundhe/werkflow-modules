from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdatePullRequestTitleRequest(BaseModel):
    pullRequestId: StrictStr
    title: StrictStr
