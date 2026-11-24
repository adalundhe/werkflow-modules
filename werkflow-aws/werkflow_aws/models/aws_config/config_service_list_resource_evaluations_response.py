from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_resource_evaluation import ConfigServiceResourceEvaluation


class ConfigServiceListResourceEvaluationsResponse(BaseModel):
    ResourceEvaluations: list[ConfigServiceResourceEvaluation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
