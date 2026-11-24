from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_commit_approval_rule import CodeCommitApprovalRule
from .code_commit_pull_request_target import CodeCommitPullRequestTarget


class CodeCommitPullRequest(BaseModel):
    pullRequestId: StrictStr | None = None
    title: StrictStr | None = None
    description: StrictStr | None = None
    lastActivityDate: datetime.datetime | StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    pullRequestStatus: StrictStr | None = None
    authorArn: StrictStr | None = None
    pullRequestTargets: list[CodeCommitPullRequestTarget] | None = None
    clientRequestToken: StrictStr | None = None
    revisionId: StrictStr | None = None
    approvalRules: list[CodeCommitApprovalRule] | None = None
