from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_tag import DMSTag


class DMSCreateInstanceProfileRequest(BaseModel):
    AvailabilityZone: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    PubliclyAccessible: StrictBool | None = None
    Tags: list[DMSTag] | None = None
    NetworkType: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    Description: StrictStr | None = None
    SubnetGroupIdentifier: StrictStr | None = None
    VpcSecurityGroups: list[StrictStr] | None = None
