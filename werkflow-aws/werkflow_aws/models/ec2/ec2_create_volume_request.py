from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator import EC2Operator
from .ec2_tag_specification import EC2TagSpecification
from .ec2_volume_type import EC2VolumeType


class EC2CreateVolumeRequest(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Encrypted: StrictBool | None = None
    Iops: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    Size: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    VolumeType: EC2VolumeType | None = None
    TagSpecifications: list[EC2TagSpecification] | None = None
    MultiAttachEnabled: StrictBool | None = None
    Throughput: StrictInt | None = None
    ClientToken: StrictStr | None = None
    Operator: EC2Operator | None = None
    DryRun: StrictBool | None = None
