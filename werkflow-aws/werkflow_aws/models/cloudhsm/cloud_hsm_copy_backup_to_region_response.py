from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_hsm_destination_backup import CloudHSMDestinationBackup


class CloudHSMCopyBackupToRegionResponse(BaseModel):
    DestinationBackup: CloudHSMDestinationBackup | None = None
    ResponseMetadata: dict[str, Any] | None = None
