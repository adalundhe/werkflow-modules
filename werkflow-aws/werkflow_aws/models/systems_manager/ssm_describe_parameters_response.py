from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_parameter_metadata import SSMParameterMetadata


class SSMDescribeParametersResponse(BaseModel):
    Parameters: list[SSMParameterMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
