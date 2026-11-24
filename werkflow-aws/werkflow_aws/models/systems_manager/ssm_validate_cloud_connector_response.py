from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_validation_finding import SSMValidationFinding


class SSMValidateCloudConnectorResponse(BaseModel):
    ValidationFindings: list[SSMValidationFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
