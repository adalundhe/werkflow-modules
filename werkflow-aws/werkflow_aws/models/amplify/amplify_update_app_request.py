from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_auto_branch_creation_config import AmplifyAutoBranchCreationConfig
from .amplify_cache_config import AmplifyCacheConfig
from .amplify_custom_rule import AmplifyCustomRule
from .amplify_job_config import AmplifyJobConfig


class AmplifyUpdateAppRequest(BaseModel):
    appId: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    platform: Literal['WEB', 'WEB_DYNAMIC', 'WEB_COMPUTE'] | None = None
    computeRoleArn: StrictStr | None = None
    iamServiceRoleArn: StrictStr | None = None
    environmentVariables: dict[StrictStr, StrictStr] | None = None
    enableBranchAutoBuild: StrictBool | None = None
    enableBranchAutoDeletion: StrictBool | None = None
    enableBasicAuth: StrictBool | None = None
    basicAuthCredentials: StrictStr | None = None
    customRules: list[AmplifyCustomRule] | None = None
    buildSpec: StrictStr | None = None
    customHeaders: StrictStr | None = None
    enableAutoBranchCreation: StrictBool | None = None
    autoBranchCreationPatterns: list[StrictStr] | None = None
    autoBranchCreationConfig: AmplifyAutoBranchCreationConfig | None = None
    repository: StrictStr | None = None
    oauthToken: StrictStr | None = None
    accessToken: StrictStr | None = None
    jobConfig: AmplifyJobConfig | None = None
    cacheConfig: AmplifyCacheConfig | None = None
