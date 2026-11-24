from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_evaluation_attribute_and_condition import ConnectContactEvaluationAttributeAndCondition
from .connect_contact_evaluation_attribute_condition import ConnectContactEvaluationAttributeCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectContactEvaluationAttributeFilter(BaseModel):
    OrConditions: list[ConnectContactEvaluationAttributeAndCondition] | None = None
    AndCondition: ConnectContactEvaluationAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
    ContactEvaluationAttributeCondition: ConnectContactEvaluationAttributeCondition | None = None
