from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_rule_compliance import ConfigServiceConformancePackRuleCompliance


class ConfigServiceDescribeConformancePackComplianceResponse(BaseModel):
    ConformancePackName: StrictStr | None = None
    ConformancePackRuleComplianceList: list[ConfigServiceConformancePackRuleCompliance] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
