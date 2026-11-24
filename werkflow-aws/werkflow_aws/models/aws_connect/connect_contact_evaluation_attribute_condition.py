from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_contact_evaluation_attribute_value import ConnectContactEvaluationAttributeValue


class ConnectContactEvaluationAttributeCondition(BaseModel):
    AttributeKey: Literal['ContactAgentId'] | None = None
    AttributeValue: ConnectContactEvaluationAttributeValue | None = None
    ComparisonType: Literal['EXACT'] | None = None
