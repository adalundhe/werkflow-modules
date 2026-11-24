from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueBatchGetTableOptimizerEntry(BaseModel):
    catalogId: StrictStr | None = None
    databaseName: StrictStr | None = None
    tableName: StrictStr | None = None
    type: Literal['compaction', 'retention', 'orphan_file_deletion'] | None = None
