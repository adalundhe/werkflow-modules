from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .directory_service_directory_connect_settings_description import DirectoryServiceDirectoryConnectSettingsDescription
from .directory_service_directory_vpc_settings_description import DirectoryServiceDirectoryVpcSettingsDescription
from .directory_service_hybrid_settings_description import DirectoryServiceHybridSettingsDescription
from .directory_service_owner_directory_description import DirectoryServiceOwnerDirectoryDescription
from .directory_service_radius_settings import DirectoryServiceRadiusSettings
from .directory_service_regions_info import DirectoryServiceRegionsInfo


class DirectoryServiceDirectoryDescription(BaseModel):
    DirectoryId: StrictStr | None = None
    Name: StrictStr | None = None
    ShortName: StrictStr | None = None
    Size: StrictStr | None = None
    Edition: StrictStr | None = None
    Alias: StrictStr | None = None
    AccessUrl: StrictStr | None = None
    Description: StrictStr | None = None
    DnsIpAddrs: list[StrictStr] | None = None
    DnsIpv6Addrs: list[StrictStr] | None = None
    Stage: StrictStr | None = None
    ShareStatus: StrictStr | None = None
    ShareMethod: StrictStr | None = None
    ShareNotes: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    StageLastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    VpcSettings: DirectoryServiceDirectoryVpcSettingsDescription | None = None
    ConnectSettings: DirectoryServiceDirectoryConnectSettingsDescription | None = None
    RadiusSettings: DirectoryServiceRadiusSettings | None = None
    RadiusStatus: StrictStr | None = None
    StageReason: StrictStr | None = None
    SsoEnabled: StrictBool | None = None
    DesiredNumberOfDomainControllers: StrictInt | None = None
    OwnerDirectoryDescription: DirectoryServiceOwnerDirectoryDescription | None = None
    RegionsInfo: DirectoryServiceRegionsInfo | None = None
    OsVersion: StrictStr | None = None
    HybridSettings: DirectoryServiceHybridSettingsDescription | None = None
    NetworkType: StrictStr | None = None
