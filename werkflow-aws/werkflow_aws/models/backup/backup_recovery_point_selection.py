from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_date_range import BackupDateRange


class BackupRecoveryPointSelection(BaseModel):
    VaultNames: list[StrictStr] | None = None
    ResourceIdentifiers: list[StrictStr] | None = None
    DateRange: BackupDateRange | None = None
