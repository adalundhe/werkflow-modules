from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_organizational_unit import SSMResourceDataSyncOrganizationalUnit


class SSMResourceDataSyncAwsOrganizationsSource(BaseModel):
    OrganizationSourceType: StrictStr | None = None
    OrganizationalUnits: list[SSMResourceDataSyncOrganizationalUnit] | None = None
