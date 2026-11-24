from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_selections_list_member import BackupSelectionsListMember


class BackupListBackupSelectionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    BackupSelectionsList: list[BackupSelectionsListMember] | None = None
    ResponseMetadata: dict[str, Any] | None = None
