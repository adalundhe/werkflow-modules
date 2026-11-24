from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_compliance_by_config_rule import ConfigServiceAggregateComplianceByConfigRule


class ConfigServiceDescribeAggregateComplianceByConfigRulesResponse(BaseModel):
    AggregateComplianceByConfigRules: list[ConfigServiceAggregateComplianceByConfigRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
