from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_action_condition import WAFv2ActionCondition
from .wa_fv2_label_name_condition import WAFv2LabelNameCondition


class WAFv2Condition(BaseModel):
    ActionCondition: WAFv2ActionCondition | None = None
    LabelNameCondition: WAFv2LabelNameCondition | None = None
