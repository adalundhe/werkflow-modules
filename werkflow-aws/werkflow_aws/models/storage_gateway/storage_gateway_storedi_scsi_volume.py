from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .storage_gateway_volumei_scsi_attributes import StorageGatewayVolumeiSCSIAttributes


class StorageGatewayStorediSCSIVolume(BaseModel):
    VolumeARN: StrictStr | None = None
    VolumeId: StrictStr | None = None
    VolumeType: StrictStr | None = None
    VolumeStatus: StrictStr | None = None
    VolumeAttachmentStatus: StrictStr | None = None
    VolumeSizeInBytes: StrictInt | None = None
    VolumeProgress: StrictFloat | StrictInt | None = None
    VolumeDiskId: StrictStr | None = None
    SourceSnapshotId: StrictStr | None = None
    PreservedExistingData: StrictBool | None = None
    VolumeiSCSIAttributes: StorageGatewayVolumeiSCSIAttributes | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    VolumeUsedInBytes: StrictInt | None = None
    KMSKey: StrictStr | None = None
    TargetName: StrictStr | None = None
