from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_directory_vpc_settings_description import DirectoryServiceDirectoryVpcSettingsDescription
from .directory_service_radius_settings import DirectoryServiceRadiusSettings


class DirectoryServiceOwnerDirectoryDescription(BaseModel):
    DirectoryId: StrictStr | None = None
    AccountId: StrictStr | None = None
    DnsIpAddrs: list[StrictStr] | None = None
    DnsIpv6Addrs: list[StrictStr] | None = None
    VpcSettings: DirectoryServiceDirectoryVpcSettingsDescription | None = None
    RadiusSettings: DirectoryServiceRadiusSettings | None = None
    RadiusStatus: StrictStr | None = None
    NetworkType: StrictStr | None = None
