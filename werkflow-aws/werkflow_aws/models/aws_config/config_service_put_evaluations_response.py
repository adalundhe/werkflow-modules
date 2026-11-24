from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_evaluation import ConfigServiceEvaluation


class ConfigServicePutEvaluationsResponse(BaseModel):
    FailedEvaluations: list[ConfigServiceEvaluation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
