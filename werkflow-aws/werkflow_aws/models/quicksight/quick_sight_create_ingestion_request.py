from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightCreateIngestionRequest(BaseModel):
    DataSetId: StrictStr
    IngestionId: StrictStr
    AwsAccountId: StrictStr
    IngestionType: Literal['INCREMENTAL_REFRESH', 'FULL_REFRESH'] | None = None
