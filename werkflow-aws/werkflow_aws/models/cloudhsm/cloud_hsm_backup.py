from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_hsm_tag import CloudHSMTag


class CloudHSMBackup(BaseModel):
    BackupId: StrictStr | None = None
    BackupArn: StrictStr | None = None
    BackupState: StrictStr | None = None
    ClusterId: StrictStr | None = None
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    CopyTimestamp: datetime.datetime | StrictStr | None = None
    NeverExpires: StrictBool | None = None
    SourceRegion: StrictStr | None = None
    SourceBackup: StrictStr | None = None
    SourceCluster: StrictStr | None = None
    DeleteTimestamp: datetime.datetime | StrictStr | None = None
    TagList: list[CloudHSMTag] | None = None
    HsmType: StrictStr | None = None
    Mode: StrictStr | None = None
