from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_rule import ConnectRule


class ConnectDescribeRuleResponse(BaseModel):
    Rule: ConnectRule | None = None
    ResponseMetadata: dict[str, Any] | None = None
