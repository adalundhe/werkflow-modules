from __future__ import annotations
from pydantic import BaseModel
from .io_t_policy import IoTPolicy


class IoTExplicitDeny(BaseModel):
    policies: list[IoTPolicy] | None = None
