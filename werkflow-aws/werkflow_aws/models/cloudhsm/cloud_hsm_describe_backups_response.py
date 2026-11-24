from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_hsm_backup import CloudHSMBackup


class CloudHSMDescribeBackupsResponse(BaseModel):
    Backups: list[CloudHSMBackup] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
