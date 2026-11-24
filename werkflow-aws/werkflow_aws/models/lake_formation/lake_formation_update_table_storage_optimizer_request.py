from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LakeFormationUpdateTableStorageOptimizerRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    StorageOptimizerConfig: dict[Literal['COMPACTION', 'GARBAGE_COLLECTION', 'ALL'], dict[StrictStr, StrictStr]]
    CatalogId: StrictStr | None = None
