from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueAutoDataQuality(BaseModel):
    IsEnabled: StrictBool | None = None
    EvaluationContext: StrictStr | None = None
