from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDirectoryVpcSettingsDescription(BaseModel):
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupId: StrictStr | None = None
    AvailabilityZones: list[StrictStr] | None = None
