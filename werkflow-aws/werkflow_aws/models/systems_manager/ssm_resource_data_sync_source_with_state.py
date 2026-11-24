from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_resource_data_sync_aws_organizations_source import SSMResourceDataSyncAwsOrganizationsSource


class SSMResourceDataSyncSourceWithState(BaseModel):
    SourceType: StrictStr | None = None
    AwsOrganizationsSource: SSMResourceDataSyncAwsOrganizationsSource | None = None
    SourceRegions: list[StrictStr] | None = None
    IncludeFutureRegions: StrictBool | None = None
    State: StrictStr | None = None
    EnableAllOpsDataSources: StrictBool | None = None
