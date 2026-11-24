from __future__ import annotations
from pydantic import BaseModel
from .connect_expression import ConnectExpression
from .connect_routing_criteria_input_step_expiry import ConnectRoutingCriteriaInputStepExpiry


class ConnectRoutingCriteriaInputStep(BaseModel):
    Expiry: ConnectRoutingCriteriaInputStepExpiry | None = None
    Expression: ConnectExpression | None = None
