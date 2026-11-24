from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListTableOptimizerRunsRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    Type: Literal['compaction', 'retention', 'orphan_file_deletion']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
