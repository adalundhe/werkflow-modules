from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_activation import SSMActivation


class SSMDescribeActivationsResponse(BaseModel):
    ActivationList: list[SSMActivation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
