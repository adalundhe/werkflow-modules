from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_item_enablement_condition import ConnectEvaluationFormItemEnablementCondition


class ConnectEvaluationFormItemEnablementConfiguration(BaseModel):
    Condition: ConnectEvaluationFormItemEnablementCondition | None = None
    Action: StrictStr | None = None
    DefaultAction: StrictStr | None = None
