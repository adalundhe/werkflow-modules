from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSModifyInstanceProfileRequest(BaseModel):
    InstanceProfileIdentifier: StrictStr
    AvailabilityZone: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    NetworkType: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    Description: StrictStr | None = None
    SubnetGroupIdentifier: StrictStr | None = None
    VpcSecurityGroups: list[StrictStr] | None = None
