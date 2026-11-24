from __future__ import annotations
from pydantic import BaseModel
from .io_t_behavior import IoTBehavior


class IoTValidateSecurityProfileBehaviorsRequest(BaseModel):
    behaviors: list[IoTBehavior]
