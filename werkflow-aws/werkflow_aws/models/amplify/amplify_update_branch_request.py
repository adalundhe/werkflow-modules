from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_backend import AmplifyBackend


class AmplifyUpdateBranchRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    description: StrictStr | None = None
    framework: StrictStr | None = None
    stage: Literal['PRODUCTION', 'BETA', 'DEVELOPMENT', 'EXPERIMENTAL', 'PULL_REQUEST'] | None = None
    enableNotification: StrictBool | None = None
    enableAutoBuild: StrictBool | None = None
    enableSkewProtection: StrictBool | None = None
    environmentVariables: dict[StrictStr, StrictStr] | None = None
    basicAuthCredentials: StrictStr | None = None
    enableBasicAuth: StrictBool | None = None
    enablePerformanceMode: StrictBool | None = None
    buildSpec: StrictStr | None = None
    ttl: StrictStr | None = None
    displayName: StrictStr | None = None
    enablePullRequestPreview: StrictBool | None = None
    pullRequestEnvironmentName: StrictStr | None = None
    backendEnvironmentArn: StrictStr | None = None
    backend: AmplifyBackend | None = None
    computeRoleArn: StrictStr | None = None
