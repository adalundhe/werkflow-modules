from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupRestoreTestingRecoveryPointSelection(BaseModel):
    Algorithm: StrictStr | None = None
    ExcludeVaults: list[StrictStr] | None = None
    IncludeVaults: list[StrictStr] | None = None
    RecoveryPointTypes: list[StrictStr] | None = None
    SelectionWindowDays: StrictInt | None = None
