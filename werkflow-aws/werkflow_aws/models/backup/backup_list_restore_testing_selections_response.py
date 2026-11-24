from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_selection_for_list import BackupRestoreTestingSelectionForList


class BackupListRestoreTestingSelectionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    RestoreTestingSelections: list[BackupRestoreTestingSelectionForList] | None = None
    ResponseMetadata: dict[str, Any] | None = None
