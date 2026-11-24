from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_item_enablement_condition_operand import ConnectEvaluationFormItemEnablementConditionOperand


class ConnectEvaluationFormItemEnablementCondition(BaseModel):
    Operands: list[ConnectEvaluationFormItemEnablementConditionOperand] | None = None
    Operator: StrictStr | None = None
