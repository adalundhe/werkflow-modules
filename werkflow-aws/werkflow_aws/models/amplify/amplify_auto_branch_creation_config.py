from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AmplifyAutoBranchCreationConfig(BaseModel):
    stage: StrictStr | None = None
    framework: StrictStr | None = None
    enableAutoBuild: StrictBool | None = None
    environmentVariables: dict[StrictStr, StrictStr] | None = None
    basicAuthCredentials: StrictStr | None = None
    enableBasicAuth: StrictBool | None = None
    enablePerformanceMode: StrictBool | None = None
    buildSpec: StrictStr | None = None
    enablePullRequestPreview: StrictBool | None = None
    pullRequestEnvironmentName: StrictStr | None = None
