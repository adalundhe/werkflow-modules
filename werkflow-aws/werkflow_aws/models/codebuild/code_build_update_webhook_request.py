from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .code_build_pull_request_build_policy import CodeBuildPullRequestBuildPolicy
from .code_build_webhook_filter import CodeBuildWebhookFilter


class CodeBuildUpdateWebhookRequest(BaseModel):
    projectName: StrictStr
    branchFilter: StrictStr | None = None
    rotateSecret: StrictBool | None = None
    filterGroups: list[list[CodeBuildWebhookFilter]] | None = None
    buildType: Literal['BUILD', 'BUILD_BATCH', 'RUNNER_BUILDKITE_BUILD'] | None = None
    pullRequestBuildPolicy: CodeBuildPullRequestBuildPolicy | None = None
