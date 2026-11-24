from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdatePullRequestDescriptionRequest(BaseModel):
    pullRequestId: StrictStr
    description: StrictStr
