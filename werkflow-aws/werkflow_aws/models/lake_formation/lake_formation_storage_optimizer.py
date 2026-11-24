from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationStorageOptimizer(BaseModel):
    StorageOptimizerType: StrictStr | None = None
    Config: dict[StrictStr, StrictStr] | None = None
    ErrorMessage: StrictStr | None = None
    Warnings: StrictStr | None = None
    LastRunDetails: StrictStr | None = None
