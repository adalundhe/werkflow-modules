from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_remediation_filters import SecurityHubRemediationFilters


class SecurityHubGetRemediationsV2Request(BaseModel):
    TargetUid: StrictStr | None = None
    MetadataUid: StrictStr | None = None
    Filters: SecurityHubRemediationFilters | None = None
    ShowGuidance: StrictBool | None = None
    GuidanceFormat: Literal['All', 'AwsCli', 'Cli', 'Python', 'Terraform', 'Cdk', 'CloudFormation', 'IaC', 'Template'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
