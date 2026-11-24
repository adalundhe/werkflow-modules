from __future__ import annotations
from pydantic import BaseModel
from .connect_routing_criteria_input_step import ConnectRoutingCriteriaInputStep


class ConnectRoutingCriteriaInput(BaseModel):
    Steps: list[ConnectRoutingCriteriaInputStep] | None = None
