from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .config_service_evaluation import ConfigServiceEvaluation


class ConfigServicePutEvaluationsRequest(BaseModel):
    ResultToken: StrictStr
    Evaluations: list[ConfigServiceEvaluation] | None = None
    TestMode: StrictBool | None = None
