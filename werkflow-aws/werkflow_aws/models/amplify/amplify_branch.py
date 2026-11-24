from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_backend import AmplifyBackend


class AmplifyBranch(BaseModel):
    branchArn: StrictStr | None = None
    branchName: StrictStr | None = None
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    stage: StrictStr | None = None
    displayName: StrictStr | None = None
    enableNotification: StrictBool | None = None
    createTime: datetime.datetime | StrictStr | None = None
    updateTime: datetime.datetime | StrictStr | None = None
    environmentVariables: dict[StrictStr, StrictStr] | None = None
    enableAutoBuild: StrictBool | None = None
    enableSkewProtection: StrictBool | None = None
    customDomains: list[StrictStr] | None = None
    framework: StrictStr | None = None
    activeJobId: StrictStr | None = None
    totalNumberOfJobs: StrictStr | None = None
    enableBasicAuth: StrictBool | None = None
    enablePerformanceMode: StrictBool | None = None
    thumbnailUrl: StrictStr | None = None
    basicAuthCredentials: StrictStr | None = None
    buildSpec: StrictStr | None = None
    ttl: StrictStr | None = None
    associatedResources: list[StrictStr] | None = None
    enablePullRequestPreview: StrictBool | None = None
    pullRequestEnvironmentName: StrictStr | None = None
    destinationBranch: StrictStr | None = None
    sourceBranch: StrictStr | None = None
    backendEnvironmentArn: StrictStr | None = None
    backend: AmplifyBackend | None = None
    computeRoleArn: StrictStr | None = None
