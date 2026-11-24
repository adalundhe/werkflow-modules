from __future__ import annotations
from pydantic import BaseModel
from .connect_string_condition import ConnectStringCondition


class ConnectPromptSearchCriteria(BaseModel):
    OrConditions: list[ConnectPromptSearchCriteria] | None = None
    AndConditions: list[ConnectPromptSearchCriteria] | None = None
    StringCondition: ConnectStringCondition | None = None
