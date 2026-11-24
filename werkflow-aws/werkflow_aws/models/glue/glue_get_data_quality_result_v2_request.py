from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataQualityResultV2Request(BaseModel):
    ResultId: StrictStr
