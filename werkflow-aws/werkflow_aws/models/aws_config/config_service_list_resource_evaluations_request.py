from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_resource_evaluation_filters import ConfigServiceResourceEvaluationFilters


class ConfigServiceListResourceEvaluationsRequest(BaseModel):
    Filters: ConfigServiceResourceEvaluationFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
