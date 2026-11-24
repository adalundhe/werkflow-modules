from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_result_identifier import ConfigServiceEvaluationResultIdentifier


class ConfigServiceConformancePackEvaluationResult(BaseModel):
    ComplianceType: StrictStr | None = None
    EvaluationResultIdentifier: ConfigServiceEvaluationResultIdentifier | None = None
    ConfigRuleInvokedTime: datetime.datetime | StrictStr | None = None
    ResultRecordedTime: datetime.datetime | StrictStr | None = None
    Annotation: StrictStr | None = None
