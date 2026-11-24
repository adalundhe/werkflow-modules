from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectContactFlowModuleSearchCriteria(BaseModel):
    OrConditions: list[ConnectContactFlowModuleSearchCriteria] | None = None
    AndConditions: list[ConnectContactFlowModuleSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    StateCondition: Literal['ACTIVE', 'ARCHIVED'] | None = None
    StatusCondition: Literal['PUBLISHED', 'SAVED'] | None = None
