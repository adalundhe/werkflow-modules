from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CopySnapshotRequest(BaseModel):
    SourceRegion: StrictStr
    SourceSnapshotId: StrictStr
    Description: StrictStr | None = None
    DestinationOutpostArn: StrictStr | None = None
    DestinationRegion: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    PresignedUrl: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    CompletionDurationMinutes: StrictInt | None = None
    DestinationAvailabilityZone: StrictStr | None = None
    DryRun: StrictBool | None = None
