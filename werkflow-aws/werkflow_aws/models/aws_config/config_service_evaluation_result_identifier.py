from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_result_qualifier import ConfigServiceEvaluationResultQualifier


class ConfigServiceEvaluationResultIdentifier(BaseModel):
    EvaluationResultQualifier: ConfigServiceEvaluationResultQualifier | None = None
    OrderingTimestamp: datetime.datetime | StrictStr | None = None
    ResourceEvaluationId: StrictStr | None = None
