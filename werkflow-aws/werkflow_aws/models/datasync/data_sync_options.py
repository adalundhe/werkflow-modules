from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataSyncOptions(BaseModel):
    VerifyMode: StrictStr | None = None
    OverwriteMode: StrictStr | None = None
    Atime: StrictStr | None = None
    Mtime: StrictStr | None = None
    Uid: StrictStr | None = None
    Gid: StrictStr | None = None
    PreserveDeletedFiles: StrictStr | None = None
    PreserveDevices: StrictStr | None = None
    PosixPermissions: StrictStr | None = None
    BytesPerSecond: StrictInt | None = None
    TaskQueueing: StrictStr | None = None
    LogLevel: StrictStr | None = None
    TransferMode: StrictStr | None = None
    SecurityDescriptorCopyFlags: StrictStr | None = None
    ObjectTags: StrictStr | None = None
    ObjectMetadata: StrictStr | None = None
