from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_parameter import SSMParameter


class SSMGetParametersResponse(BaseModel):
    Parameters: list[SSMParameter] | None = None
    InvalidParameters: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
