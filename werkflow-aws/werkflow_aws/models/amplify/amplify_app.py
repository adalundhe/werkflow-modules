from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_auto_branch_creation_config import AmplifyAutoBranchCreationConfig
from .amplify_cache_config import AmplifyCacheConfig
from .amplify_custom_rule import AmplifyCustomRule
from .amplify_job_config import AmplifyJobConfig
from .amplify_production_branch import AmplifyProductionBranch
from .amplify_waf_configuration import AmplifyWafConfiguration


class AmplifyApp(BaseModel):
    appId: StrictStr | None = None
    appArn: StrictStr | None = None
    name: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    description: StrictStr | None = None
    repository: StrictStr | None = None
    platform: StrictStr | None = None
    createTime: datetime.datetime | StrictStr | None = None
    updateTime: datetime.datetime | StrictStr | None = None
    computeRoleArn: StrictStr | None = None
    iamServiceRoleArn: StrictStr | None = None
    environmentVariables: dict[StrictStr, StrictStr] | None = None
    defaultDomain: StrictStr | None = None
    enableBranchAutoBuild: StrictBool | None = None
    enableBranchAutoDeletion: StrictBool | None = None
    enableBasicAuth: StrictBool | None = None
    basicAuthCredentials: StrictStr | None = None
    customRules: list[AmplifyCustomRule] | None = None
    productionBranch: AmplifyProductionBranch | None = None
    buildSpec: StrictStr | None = None
    customHeaders: StrictStr | None = None
    enableAutoBranchCreation: StrictBool | None = None
    autoBranchCreationPatterns: list[StrictStr] | None = None
    autoBranchCreationConfig: AmplifyAutoBranchCreationConfig | None = None
    repositoryCloneMethod: StrictStr | None = None
    cacheConfig: AmplifyCacheConfig | None = None
    webhookCreateTime: datetime.datetime | StrictStr | None = None
    wafConfiguration: AmplifyWafConfiguration | None = None
    jobConfig: AmplifyJobConfig | None = None
