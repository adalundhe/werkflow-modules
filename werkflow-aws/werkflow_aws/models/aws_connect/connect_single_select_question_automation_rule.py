from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_item_enablement_condition import ConnectEvaluationFormItemEnablementCondition


class ConnectSingleSelectQuestionAutomationRule(BaseModel):
    Condition: ConnectEvaluationFormItemEnablementCondition | None = None
    OptionRefId: StrictStr | None = None
