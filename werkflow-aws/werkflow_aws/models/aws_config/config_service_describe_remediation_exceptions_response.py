from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_remediation_exception import ConfigServiceRemediationException


class ConfigServiceDescribeRemediationExceptionsResponse(BaseModel):
    RemediationExceptions: list[ConfigServiceRemediationException] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
