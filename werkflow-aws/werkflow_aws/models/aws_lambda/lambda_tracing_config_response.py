from __future__ import annotations
from pydantic import BaseModel
from .lambda_tracing_mode import LambdaTracingMode


class LambdaTracingConfigResponse(BaseModel):
    Mode: LambdaTracingMode | None = None
