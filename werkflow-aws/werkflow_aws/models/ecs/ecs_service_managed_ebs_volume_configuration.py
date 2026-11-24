from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecsebs_tag_specification import ECSEBSTagSpecification


class ECSServiceManagedEBSVolumeConfiguration(BaseModel):
    encrypted: StrictBool | None = None
    kmsKeyId: StrictStr | None = None
    volumeType: StrictStr | None = None
    sizeInGiB: StrictInt | None = None
    snapshotId: StrictStr | None = None
    volumeInitializationRate: StrictInt | None = None
    iops: StrictInt | None = None
    throughput: StrictInt | None = None
    tagSpecifications: list[ECSEBSTagSpecification] | None = None
    roleArn: StrictStr | None = None
    filesystemType: StrictStr | None = None
