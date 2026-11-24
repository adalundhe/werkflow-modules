from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_selection_for_update import BackupRestoreTestingSelectionForUpdate


class BackupUpdateRestoreTestingSelectionRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
    RestoreTestingSelection: BackupRestoreTestingSelectionForUpdate
    RestoreTestingSelectionName: StrictStr
