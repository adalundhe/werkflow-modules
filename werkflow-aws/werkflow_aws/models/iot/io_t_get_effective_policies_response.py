from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_effective_policy import IoTEffectivePolicy


class IoTGetEffectivePoliciesResponse(BaseModel):
    effectivePolicies: list[IoTEffectivePolicy] | None = None
    ResponseMetadata: dict[str, Any] | None = None
