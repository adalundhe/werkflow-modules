from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetCustomEntityTypesRequest(BaseModel):
    Names: list[StrictStr]
