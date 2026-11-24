from __future__ import annotations
from pydantic import BaseModel
from .backup_key_value import BackupKeyValue


class BackupProtectedResourceConditions(BaseModel):
    StringEquals: list[BackupKeyValue] | None = None
    StringNotEquals: list[BackupKeyValue] | None = None
