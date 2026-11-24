from __future__ import annotations
from pydantic import BaseModel
from .connect_number_condition import ConnectNumberCondition
from .connect_string_condition import ConnectStringCondition


class ConnectCondition(BaseModel):
    StringCondition: ConnectStringCondition | None = None
    NumberCondition: ConnectNumberCondition | None = None
