from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_compliance_by_config_rule import ConfigServiceComplianceByConfigRule


class ConfigServiceDescribeComplianceByConfigRuleResponse(BaseModel):
    ComplianceByConfigRules: list[ConfigServiceComplianceByConfigRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
