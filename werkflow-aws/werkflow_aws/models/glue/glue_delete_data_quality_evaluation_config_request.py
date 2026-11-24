from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteDataQualityEvaluationConfigRequest(BaseModel):
    Name: StrictStr
