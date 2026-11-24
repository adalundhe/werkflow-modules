from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .efs_tag import EFSTag


class EFSCreateFileSystemRequest(BaseModel):
    CreationToken: StrictStr
    PerformanceMode: Literal['generalPurpose', 'maxIO'] | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    ThroughputMode: Literal['bursting', 'provisioned', 'elastic'] | None = None
    ProvisionedThroughputInMibps: StrictFloat | StrictInt | None = None
    AvailabilityZoneName: StrictStr | None = None
    Backup: StrictBool | None = None
    Tags: list[EFSTag] | None = None
