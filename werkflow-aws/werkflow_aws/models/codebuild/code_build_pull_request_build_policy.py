from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildPullRequestBuildPolicy(BaseModel):
    requiresCommentApproval: StrictStr | None = None
    approverRoles: list[StrictStr] | None = None
