from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTCreatePolicyRequest(BaseModel):
    policyName: StrictStr
    policyDocument: StrictStr
    tags: list[IoTTag] | None = None
