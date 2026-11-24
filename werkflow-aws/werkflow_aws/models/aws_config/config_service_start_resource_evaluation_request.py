from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_evaluation_context import ConfigServiceEvaluationContext
from .config_service_resource_details import ConfigServiceResourceDetails


class ConfigServiceStartResourceEvaluationRequest(BaseModel):
    ResourceDetails: ConfigServiceResourceDetails
    EvaluationMode: Literal['DETECTIVE', 'PROACTIVE']
    EvaluationContext: ConfigServiceEvaluationContext | None = None
    EvaluationTimeout: StrictInt | None = None
    ClientToken: StrictStr | None = None
