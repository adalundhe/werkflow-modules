from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetDataQualityResultV2Request(BaseModel):
    ResultIds: list[StrictStr]
