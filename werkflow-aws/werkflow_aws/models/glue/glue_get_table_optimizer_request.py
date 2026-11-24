from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueGetTableOptimizerRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    Type: Literal['compaction', 'retention', 'orphan_file_deletion']
