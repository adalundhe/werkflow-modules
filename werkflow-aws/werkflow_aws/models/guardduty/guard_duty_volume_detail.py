from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyVolumeDetail(BaseModel):
    VolumeArn: StrictStr | None = None
    VolumeType: StrictStr | None = None
    DeviceName: StrictStr | None = None
    VolumeSizeInGB: StrictInt | None = None
    EncryptionType: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
