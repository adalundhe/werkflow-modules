from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_rule_evaluation_status import SageMakerRuleEvaluationStatus


class SageMakerDebugRuleEvaluationStatus(BaseModel):
    RuleConfigurationName: StrictStr | None = None
    RuleEvaluationJobArn: StrictStr | None = None
    RuleEvaluationStatus: SageMakerRuleEvaluationStatus | None = None
    StatusDetails: StrictStr | None = None
    LastModifiedTime: datetime.datetime | None = None
