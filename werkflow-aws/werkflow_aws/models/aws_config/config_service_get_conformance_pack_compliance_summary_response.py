from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_compliance_summary import ConfigServiceConformancePackComplianceSummary


class ConfigServiceGetConformancePackComplianceSummaryResponse(BaseModel):
    ConformancePackComplianceSummaryList: list[ConfigServiceConformancePackComplianceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
