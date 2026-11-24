from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectQueueSearchCriteria(BaseModel):
    OrConditions: list[ConnectQueueSearchCriteria] | None = None
    AndConditions: list[ConnectQueueSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
    QueueTypeCondition: Literal['STANDARD'] | None = None
