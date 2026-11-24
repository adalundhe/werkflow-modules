from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_resource_selection import BackupResourceSelection


class BackupTieringConfigurationInputForCreate(BaseModel):
    TieringConfigurationName: StrictStr
    BackupVaultName: StrictStr
    ResourceSelection: list[BackupResourceSelection]
