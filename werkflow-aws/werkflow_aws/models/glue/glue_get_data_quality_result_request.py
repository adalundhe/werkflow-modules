from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataQualityResultRequest(BaseModel):
    ResultId: StrictStr
