from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineEvaluateExpressionRequest(BaseModel):
    pipelineId: StrictStr
    objectId: StrictStr
    expression: StrictStr
