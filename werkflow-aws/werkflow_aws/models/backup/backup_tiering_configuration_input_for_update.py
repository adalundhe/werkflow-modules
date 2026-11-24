from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_resource_selection import BackupResourceSelection


class BackupTieringConfigurationInputForUpdate(BaseModel):
    ResourceSelection: list[BackupResourceSelection]
    BackupVaultName: StrictStr
