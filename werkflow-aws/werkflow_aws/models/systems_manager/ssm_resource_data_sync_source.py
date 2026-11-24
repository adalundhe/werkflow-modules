from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_resource_data_sync_aws_organizations_source import SSMResourceDataSyncAwsOrganizationsSource


class SSMResourceDataSyncSource(BaseModel):
    SourceType: StrictStr
    SourceRegions: list[StrictStr]
    AwsOrganizationsSource: SSMResourceDataSyncAwsOrganizationsSource | None = None
    IncludeFutureRegions: StrictBool | None = None
    EnableAllOpsDataSources: StrictBool | None = None
