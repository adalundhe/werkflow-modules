from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueCreateDataQualityEvaluationConfigResponse(BaseModel):
    Name: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
