from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class DMSInstanceProfile(BaseModel):
    InstanceProfileArn: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    NetworkType: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    Description: StrictStr | None = None
    InstanceProfileCreationTime: datetime.datetime | StrictStr | None = None
    SubnetGroupIdentifier: StrictStr | None = None
    VpcSecurityGroups: list[StrictStr] | None = None
