from __future__ import annotations
from pydantic import BaseModel
from .connect_attribute_condition import ConnectAttributeCondition


class ConnectExpression(BaseModel):
    AttributeCondition: ConnectAttributeCondition | None = None
    AndExpression: list[ConnectExpression] | None = None
    OrExpression: list[ConnectExpression] | None = None
    NotAttributeCondition: ConnectAttributeCondition | None = None
