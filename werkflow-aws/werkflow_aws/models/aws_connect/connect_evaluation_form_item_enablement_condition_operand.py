from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel
from .connect_evaluation_form_item_enablement_expression import ConnectEvaluationFormItemEnablementExpression

if TYPE_CHECKING:
    from .connect_evaluation_form_item_enablement_condition import ConnectEvaluationFormItemEnablementCondition


class ConnectEvaluationFormItemEnablementConditionOperand(BaseModel):
    Expression: ConnectEvaluationFormItemEnablementExpression | None = None
    Condition: ConnectEvaluationFormItemEnablementCondition | None = None
