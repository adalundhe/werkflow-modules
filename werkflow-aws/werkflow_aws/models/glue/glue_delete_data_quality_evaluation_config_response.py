from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class GlueDeleteDataQualityEvaluationConfigResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
