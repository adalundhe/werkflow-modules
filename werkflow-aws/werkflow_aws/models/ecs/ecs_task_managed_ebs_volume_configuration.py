from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecsebs_tag_specification import ECSEBSTagSpecification
from .ecs_task_managed_ebs_volume_termination_policy import ECSTaskManagedEBSVolumeTerminationPolicy


class ECSTaskManagedEBSVolumeConfiguration(BaseModel):
    roleArn: StrictStr
    encrypted: StrictBool | None = None
    kmsKeyId: StrictStr | None = None
    volumeType: StrictStr | None = None
    sizeInGiB: StrictInt | None = None
    snapshotId: StrictStr | None = None
    volumeInitializationRate: StrictInt | None = None
    iops: StrictInt | None = None
    throughput: StrictInt | None = None
    tagSpecifications: list[ECSEBSTagSpecification] | None = None
    terminationPolicy: ECSTaskManagedEBSVolumeTerminationPolicy | None = None
    filesystemType: Literal['ext3', 'ext4', 'xfs', 'ntfs'] | None = None
