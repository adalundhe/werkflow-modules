from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartMLEvaluationTaskRunRequest(BaseModel):
    TransformId: StrictStr
