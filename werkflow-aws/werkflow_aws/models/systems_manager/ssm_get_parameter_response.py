from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_parameter import SSMParameter


class SSMGetParameterResponse(BaseModel):
    Parameter: SSMParameter | None = None
    ResponseMetadata: dict[str, Any] | None = None
