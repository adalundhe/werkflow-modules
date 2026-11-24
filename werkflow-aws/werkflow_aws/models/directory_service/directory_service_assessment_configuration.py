from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_directory_vpc_settings import DirectoryServiceDirectoryVpcSettings


class DirectoryServiceAssessmentConfiguration(BaseModel):
    CustomerDnsIps: list[StrictStr]
    DnsName: StrictStr
    VpcSettings: DirectoryServiceDirectoryVpcSettings
    InstanceIds: list[StrictStr]
    SecurityGroupIds: list[StrictStr] | None = None
