from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .code_build_pull_request_build_policy import CodeBuildPullRequestBuildPolicy
from .code_build_scope_configuration import CodeBuildScopeConfiguration
from .code_build_webhook_filter import CodeBuildWebhookFilter


class CodeBuildWebhook(BaseModel):
    url: StrictStr | None = None
    payloadUrl: StrictStr | None = None
    secret: StrictStr | None = None
    branchFilter: StrictStr | None = None
    filterGroups: list[list[CodeBuildWebhookFilter]] | None = None
    buildType: StrictStr | None = None
    manualCreation: StrictBool | None = None
    lastModifiedSecret: datetime.datetime | StrictStr | None = None
    scopeConfiguration: CodeBuildScopeConfiguration | None = None
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
    pullRequestBuildPolicy: CodeBuildPullRequestBuildPolicy | None = None
