from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_restore_testing_selection_for_create import BackupRestoreTestingSelectionForCreate


class BackupCreateRestoreTestingSelectionRequest(BaseModel):
    RestoreTestingPlanName: StrictStr
    RestoreTestingSelection: BackupRestoreTestingSelectionForCreate
    CreatorRequestId: StrictStr | None = None
