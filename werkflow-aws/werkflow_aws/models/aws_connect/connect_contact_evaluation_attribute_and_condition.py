from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_evaluation_attribute_condition import ConnectContactEvaluationAttributeCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectContactEvaluationAttributeAndCondition(BaseModel):
    TagConditions: list[ConnectTagCondition] | None = None
    AttributeConditions: list[ConnectContactEvaluationAttributeCondition] | None = None
