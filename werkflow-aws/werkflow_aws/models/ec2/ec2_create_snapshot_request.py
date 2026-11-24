from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification import EC2TagSpecification


class EC2CreateSnapshotRequest(BaseModel):
    VolumeId: StrictStr
    Description: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecification] | None = None
    DryRun: StrictBool | None = None
