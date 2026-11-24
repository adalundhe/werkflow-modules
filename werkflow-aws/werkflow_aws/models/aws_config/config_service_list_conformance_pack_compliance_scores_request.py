from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_conformance_pack_compliance_scores_filters import ConfigServiceConformancePackComplianceScoresFilters


class ConfigServiceListConformancePackComplianceScoresRequest(BaseModel):
    Filters: ConfigServiceConformancePackComplianceScoresFilters | None = None
    SortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    SortBy: Literal['SCORE'] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
