from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_granular_access_control_configuration import ConnectGranularAccessControlConfiguration


class ConnectSecurityProfile(BaseModel):
    Id: StrictStr | None = None
    OrganizationResourceId: StrictStr | None = None
    Arn: StrictStr | None = None
    SecurityProfileName: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    AllowedAccessControlTags: dict[StrictStr, StrictStr] | None = None
    TagRestrictedResources: list[StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    HierarchyRestrictedResources: list[StrictStr] | None = None
    AllowedAccessControlHierarchyGroupId: StrictStr | None = None
    GranularAccessControlConfiguration: ConnectGranularAccessControlConfiguration | None = None
    Type: StrictStr | None = None
