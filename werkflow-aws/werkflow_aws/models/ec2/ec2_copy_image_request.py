from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CopyImageRequest(BaseModel):
    Name: StrictStr
    SourceImageId: StrictStr
    SourceRegion: StrictStr
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    DestinationOutpostArn: StrictStr | None = None
    CopyImageTags: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    SnapshotCopyCompletionDurationMinutes: StrictInt | None = None
    DestinationAvailabilityZone: StrictStr | None = None
    DestinationAvailabilityZoneId: StrictStr | None = None
    DryRun: StrictBool | None = None
