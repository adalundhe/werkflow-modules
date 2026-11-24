from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_parameter import SSMParameter


class SSMGetParametersByPathResponse(BaseModel):
    Parameters: list[SSMParameter] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
