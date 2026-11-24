from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_restore_testing_selection_for_get import BackupRestoreTestingSelectionForGet


class BackupGetRestoreTestingSelectionResponse(BaseModel):
    RestoreTestingSelection: BackupRestoreTestingSelectionForGet | None = None
    ResponseMetadata: dict[str, Any] | None = None
