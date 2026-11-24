from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_compliance_by_resource import ConfigServiceComplianceByResource


class ConfigServiceDescribeComplianceByResourceResponse(BaseModel):
    ComplianceByResources: list[ConfigServiceComplianceByResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
