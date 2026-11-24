from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_conformance_pack_evaluation_filters import ConfigServiceConformancePackEvaluationFilters


class ConfigServiceGetConformancePackComplianceDetailsRequest(BaseModel):
    ConformancePackName: StrictStr
    Filters: ConfigServiceConformancePackEvaluationFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
