from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .detective_datasource_package_usage_info import DetectiveDatasourcePackageUsageInfo


class DetectiveMemberDetail(BaseModel):
    AccountId: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    GraphArn: StrictStr | None = None
    MasterId: StrictStr | None = None
    AdministratorId: StrictStr | None = None
    Status: StrictStr | None = None
    DisabledReason: StrictStr | None = None
    InvitedTime: datetime.datetime | StrictStr | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
    VolumeUsageInBytes: StrictInt | None = None
    VolumeUsageUpdatedTime: datetime.datetime | StrictStr | None = None
    PercentOfGraphUtilization: StrictFloat | StrictInt | None = None
    PercentOfGraphUtilizationUpdatedTime: datetime.datetime | StrictStr | None = None
    InvitationType: StrictStr | None = None
    VolumeUsageByDatasourcePackage: dict[StrictStr, DetectiveDatasourcePackageUsageInfo] | None = None
    DatasourcePackageIngestStates: dict[StrictStr, StrictStr] | None = None
