from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .directory_service_directory_vpc_settings import DirectoryServiceDirectoryVpcSettings


class DirectoryServiceRegionDescription(BaseModel):
    DirectoryId: StrictStr | None = None
    RegionName: StrictStr | None = None
    RegionType: StrictStr | None = None
    Status: StrictStr | None = None
    VpcSettings: DirectoryServiceDirectoryVpcSettings | None = None
    DesiredNumberOfDomainControllers: StrictInt | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    StatusLastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
