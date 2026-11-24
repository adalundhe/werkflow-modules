from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerDebugRuleEvaluationStatusModel(BaseModel):
    RuleConfigurationName: StrictStr | None = None
    RuleEvaluationJobArn: StrictStr | None = None
    RuleEvaluationStatus: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
