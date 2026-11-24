from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_active_directory_backup_attributes import FSxActiveDirectoryBackupAttributes
from .f_sx_backup_failure_details import FSxBackupFailureDetails
from .f_sx_file_system import FSxFileSystem
from .f_sx_tag import FSxTag
from .f_sx_volume import FSxVolume


class FSxBackup(BaseModel):
    BackupId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    FailureDetails: FSxBackupFailureDetails | None = None
    Type: StrictStr | None = None
    ProgressPercent: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    FileSystem: FSxFileSystem | None = None
    DirectoryInformation: FSxActiveDirectoryBackupAttributes | None = None
    OwnerId: StrictStr | None = None
    SourceBackupId: StrictStr | None = None
    SourceBackupRegion: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Volume: FSxVolume | None = None
    SizeInBytes: StrictInt | None = None
