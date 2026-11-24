from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectTestCaseSearchCriteria(BaseModel):
    OrConditions: list[ConnectTestCaseSearchCriteria] | None = None
    AndConditions: list[ConnectTestCaseSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    StatusCondition: Literal['PUBLISHED', 'SAVED'] | None = None
