from __future__ import annotations
from pydantic import BaseModel
from .connect_searchable_routing_criteria_step import ConnectSearchableRoutingCriteriaStep


class ConnectSearchableRoutingCriteria(BaseModel):
    Steps: list[ConnectSearchableRoutingCriteriaStep] | None = None
