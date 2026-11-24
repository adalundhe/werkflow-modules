from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_hsm_tag import CloudHSMTag


class CloudHSMCopyBackupToRegionRequest(BaseModel):
    DestinationRegion: StrictStr
    BackupId: StrictStr
    TagList: list[CloudHSMTag] | None = None
