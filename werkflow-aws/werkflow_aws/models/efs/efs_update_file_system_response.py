from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .efs_file_system_protection_description import EFSFileSystemProtectionDescription
from .efs_file_system_size import EFSFileSystemSize
from .efs_tag import EFSTag


class EFSUpdateFileSystemResponse(BaseModel):
    OwnerId: StrictStr | None = None
    CreationToken: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    FileSystemArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LifeCycleState: StrictStr | None = None
    Name: StrictStr | None = None
    NumberOfMountTargets: StrictInt | None = None
    SizeInBytes: EFSFileSystemSize | None = None
    PerformanceMode: StrictStr | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    ThroughputMode: StrictStr | None = None
    ProvisionedThroughputInMibps: StrictFloat | StrictInt | None = None
    AvailabilityZoneName: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    Tags: list[EFSTag] | None = None
    FileSystemProtection: EFSFileSystemProtectionDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
