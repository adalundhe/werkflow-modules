from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_vault_list_member import BackupVaultListMember


class BackupListBackupVaultsResponse(BaseModel):
    BackupVaultList: list[BackupVaultListMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
