from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_external_evaluation import ConfigServiceExternalEvaluation


class ConfigServicePutExternalEvaluationRequest(BaseModel):
    ConfigRuleName: StrictStr
    ExternalEvaluation: ConfigServiceExternalEvaluation
