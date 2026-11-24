from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_result_identifier import ConfigServiceEvaluationResultIdentifier


class ConfigServiceEvaluationResult(BaseModel):
    EvaluationResultIdentifier: ConfigServiceEvaluationResultIdentifier | None = None
    ComplianceType: StrictStr | None = None
    ResultRecordedTime: datetime.datetime | StrictStr | None = None
    ConfigRuleInvokedTime: datetime.datetime | StrictStr | None = None
    Annotation: StrictStr | None = None
    ResultToken: StrictStr | None = None
