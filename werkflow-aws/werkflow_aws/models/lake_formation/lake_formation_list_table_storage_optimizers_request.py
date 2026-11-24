from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationListTableStorageOptimizersRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogId: StrictStr | None = None
    StorageOptimizerType: Literal['COMPACTION', 'GARBAGE_COLLECTION', 'ALL'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
